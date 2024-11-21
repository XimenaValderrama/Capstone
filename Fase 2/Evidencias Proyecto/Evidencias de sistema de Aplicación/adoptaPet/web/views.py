from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import re
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import *
from web.cargar_datos_fundaciones import consumir_y_guardar_fundaciones
from django.http import JsonResponse

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def modificar_eliminar_usuario(request, user_id):
    try:

        perfil_usuario = PerfilUsuario.objects.get(id=user_id)
        usuario = perfil_usuario.usuario_django
        

    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    except PerfilUsuario.DoesNotExist:
        return Response({"error": "Perfil de usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serializar los datos del usuario y perfil
        usuario_serializer = UserSerializer(usuario)
        perfil_serializer = PerfilUsuarioSerializer(perfil_usuario)
        return Response({
            "usuario": usuario_serializer.data,
            "perfil": perfil_serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        # Modificar perfil y usuario
        usuario_data = request.data.get('usuario', {})
        perfil_data = request.data.get('perfil', {})

        usuario_serializer = UserSerializer(usuario, data=usuario_data, partial=True)
        perfil_serializer = PerfilUsuarioSerializer(perfil_usuario, data=perfil_data, partial=True)
        
        # Verificar que ambos serializers son válidos antes de guardar
        if usuario_serializer.is_valid() and perfil_serializer.is_valid():
            usuario_serializer.save()
            perfil_serializer.save()
            return Response({
                "usuario": usuario_serializer.data,
                "perfil": perfil_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            # Retornar errores de validación
            errors = {
                "usuario_errors": usuario_serializer.errors if not usuario_serializer.is_valid() else {},
                "perfil_errors": perfil_serializer.errors if not perfil_serializer.is_valid() else {}
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Eliminar perfil y usuario
        usuario.delete()
        perfil_usuario.delete()
        
        return Response({"message": "Usuario y perfil eliminados correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def eliminar_usuario(request, user_profile_id):
    try:
        perfil_usuario = PerfilUsuario.objects.get(id=user_profile_id)
        usuario = perfil_usuario.usuario_django

    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    except PerfilUsuario.DoesNotExist:
        return Response({"error": "Perfil de usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    perfil_usuario.delete()
    return Response({"message": "Usuario y perfil eliminados correctamente."}, status=status.HTTP_204_NO_CONTENT)

@login_required(login_url="inicio_sesion")
def inicio(request):
    # Obtener todas las mascotas
    mascotas = Mascota.objects.all()
    
    # Pasar las mascotas al contexto del template
    context = {
        'mascotas': mascotas
    }

    return render(request, "index.html", context)

def inicio_sesion(request):    

    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST['username']
        password = request.POST['password'] 

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si las credenciales son correctas, iniciar sesión
            login(request, user)
            return redirect('inicio')  # Redirigir a una página de inicio o perfil
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.', extra_tags='contraseñas')
            return redirect('inicio_sesion')  # Redirigir de vuelta a la página de inicio de sesión

    return render(request, 'login.html')

@login_required(login_url="inicio_sesion")
def perfil(request):
    # Obtener el perfil del usuario autenticado
    usuario = get_object_or_404(PerfilUsuario, usuario_django=request.user)

    # Obtener la dirección del usuario
    direccion = DireccionUsuario.objects.filter(usuario=usuario).first()

    # Verificar si la dirección existe y obtener comuna, provincia, región, y país
    comuna = direccion.comuna if direccion else None
    provincia = comuna.provincia if comuna else None
    region = provincia.region if provincia else None
    pais = region.pais if region else None

    # Pasar los datos al template
    return render(request, "perfil.html", {
        'usuario': usuario,
        'direccion': direccion,
        'comuna': comuna,
        'provincia': provincia,
        'region': region,
        'pais': pais
    })
            
@login_required(login_url="inicio_sesion")
def tenencia_responsable(request):

    return render(request, "tenencia_responsable.html")

@login_required(login_url="inicio_sesion")
def adopcion(request):
    try:
        estado_en_adopcion = EstadoMascota.objects.get(descripcion="en_adopcion")
        mascotas = Mascota.objects.filter(estado_mascota=estado_en_adopcion)
    except EstadoMascota.DoesNotExist:
        # Si el estado "en_adopcion" no existe, define `mascotas` como una lista vacía
        mascotas = []

    return render(request, 'adopcion.html', {'mascotas': mascotas})

@login_required(login_url="inicio_sesion")
def adoptados(request):
    try:
        estado_en_adopcion = EstadoMascota.objects.get(descripcion="adoptado")
        mascotas = Mascota.objects.filter(estado_mascota=estado_en_adopcion)
    except EstadoMascota.DoesNotExist:
        # Si el estado "adoptado" no existe, define `mascotas` como una lista vacía
        mascotas = []

    return render(request, 'adoptados.html', {'mascotas': mascotas})

@login_required(login_url="inicio_sesion")
def busqueda(request):
    try:
        estado_en_adopcion = EstadoMascota.objects.get(descripcion="perdido")
        mascotas = Mascota.objects.filter(estado_mascota=estado_en_adopcion)
    except EstadoMascota.DoesNotExist:
        # Si el estado "perdido" no existe, define `mascotas` como una lista vacía
        mascotas = []

    return render(request, 'busqueda.html', {'mascotas': mascotas})

@login_required(login_url="inicio_sesion")
def encontrados(request):
    try:
        estado_en_adopcion = EstadoMascota.objects.get(descripcion="encontrado")
        mascotas = Mascota.objects.filter(estado_mascota=estado_en_adopcion)
    except EstadoMascota.DoesNotExist:
        # Si el estado "encontrado" no existe, define `mascotas` como una lista vacía
        mascotas = []

    return render(request, 'encontrados.html', {'mascotas': mascotas})

def registro(request):

    if request.method == 'POST':
        # 1. Obtener datos del formulario
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rut = request.POST['rut']
        telefono = request.POST['telefono']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        comuna = request.POST['comuna']
        genero = request.POST['genero']
        estado_economico = request.POST['estado_economico']
        calle = request.POST['calle']
        numero = request.POST['numero']
        username = email  # Usar el email como nombre de usuario


        rut_numerico = re.sub(r'[\.\-]', '', rut)

        # 2. Validar que las contraseñas coincidan
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.',  extra_tags='coincidencia_contraseñas')
            return redirect('registro')

        # 3. Validar que el correo electrónico no exista
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.',  extra_tags='correo_duplicado')
            return redirect('registro')

        # 4. Validar que el nombre de usuario (correo electrónico) no exista
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ya existe una cuenta con este correo electrónico.',  extra_tags='correo_duplicado')
            return redirect('registro')

        # 5. Validar que el RUT no exista ya registrado en otro perfil de usuario
        if PerfilUsuario.objects.filter(rut=rut).exists():
            messages.error(request, 'El RUT ya está registrado.', extra_tags='rut_duplicado')
            return redirect('registro')

        # 6. Validar la longitud de la contraseña
        if len(password1) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.', extra_tags='largo_contraseña')
            return redirect('registro')

        # 7. Validar la longitud del telefono
        if not telefono.isdigit() or len(telefono) != 9:
            messages.error(request, 'El teléfono debe contener exactamente 9 dígitos. (Toma en cuenta el 9 del incio)', extra_tags='telefono')
            return redirect('registro')

        # Validar la longitud del RUT (8 o 9 dígitos)
        if not rut_numerico.isdigit() or not (8 <= len(rut_numerico) <= 9):
            messages.error(request, 'El RUT debe contener 8 o 9 dígitos sin puntos ni guion.', extra_tags='largo_contraseña')
            return redirect('registro')

        # 9. Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=nombre, last_name=apellido)
        user.save()

        # 10. Crear el perfil de usuario
        perfilusuario = PerfilUsuario()
        perfilusuario.usuario_django = user
        perfilusuario.rut = rut
        perfilusuario.telefono = telefono
        perfilusuario.genero = Genero.objects.get(id=genero)
        perfilusuario.estado_economico = EstadoEconomico.objects.get(id=estado_economico)
        perfilusuario.save()

        # 11. Crear la dirección asociada al perfil del usuario
        direccionusuario = DireccionUsuario()
        direccionusuario.calle = calle
        direccionusuario.numero = numero
        direccionusuario.comuna = Comuna.objects.get(id=comuna)
        direccionusuario.usuario = perfilusuario  # Aquí asignamos el perfil del usuario a la dirección
        direccionusuario.save()
        
        # mensaje de éxito
        messages.success(request, '¡Registro exitoso! Tu cuenta ha sido creada satisfactoriamente.', extra_tags='registro_exitoso')
        return redirect('inicio_sesion')
    else:
        paises = Pais.objects.all()
        regiones = Region.objects.all()
        provincias = Provincia.objects.all()
        comunas = Comuna.objects.all()
        generos = Genero.objects.all()
        estadoseconomicos = EstadoEconomico.objects.all()
        
        context = {
            'paises': paises,
            'provincias': provincias,
            'regiones': regiones,
            'comunas': comunas,
            'generos': generos,
            'estadoseconomicos': estadoseconomicos
        }
        # 12. Mostrar el formulario de registro
        return render(request, 'registro.html', context)

@login_required(login_url="inicio_sesion")
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion') 

@login_required(login_url="inicio_sesion")
def registro_mascota(request):

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        tipo_edad = request.POST.get('tipo_edad')  # <-- Asegúrate de obtener el valor del tipo de edad
        imagen = request.FILES.get('imagen')  # Usar request.FILES para imágenes
        estado_mascota_id = request.POST.get('estado_mascota')
        raza_id = request.POST.get('raza')
        genero_id = request.POST.get('genero')
        tipo_id = request.POST.get('tipo')
        
        # Obtener datos de la dirección desde el formulario
        calle = request.POST.get('calle')
        numero = request.POST.get('numero')
        comuna_id = request.POST.get('comuna')

        # Obtener las descripciones
        desc_fisica = request.POST.get('desc_fisica')
        desc_personalidad = request.POST.get('desc_personalidad')
        desc_adicional = request.POST.get('desc_adicional')

        descripcion = DescripcionMascota()
        descripcion.desc_fisica = desc_fisica
        descripcion.desc_personalidad = desc_personalidad
        descripcion.desc_adicional = desc_adicional
        descripcion.save() 

        # Validar y obtener instancias de relaciones ForeignKey
        estado_mascota = EstadoMascota.objects.get(id=estado_mascota_id)
        raza = Razas.objects.get(id=raza_id)
        genero = GeneroMascota.objects.get(id=genero_id)
        tipo = TipoMascota.objects.get(id=tipo_id)
        comuna = ComunaMascota.objects.get(id=comuna_id)
        usuario = PerfilUsuario.objects.get(usuario_django=request.user)

        # Crear la nueva dirección para la mascota
        direccion = DireccionMascota()
        direccion.calle = calle
        direccion.numero = numero
        direccion.comuna = comuna
        direccion.save()

        # Crear la nueva mascota asociada con la descripción, dirección, y tipo de edad
        mascota = Mascota()
        mascota.nombre = nombre
        mascota.apellido = apellido
        mascota.edad = edad
        mascota.tipo_edad = tipo_edad
        mascota.imagen = imagen
        mascota.estado_mascota = estado_mascota
        mascota.raza = raza
        mascota.genero = genero
        mascota.descripcion = descripcion
        mascota.tipo = tipo
        mascota.direccion = direccion
        mascota.usuario = usuario
        mascota.save()
        
        messages.success(request, 'Se registro su mascota con exito.', extra_tags='registro_mascota')
        
        # Redirigir a otra página después de guardar
        return redirect('mascotas') 

    # Obtener listas de opciones para el formulario
    paises = PaisMascota.objects.all()
    regiones = RegionMascota.objects.all()
    provincias = ProvinciaMascota.objects.all()
    comunas = ComunaMascota.objects.all()
    generos = GeneroMascota.objects.all()
    estados = EstadoMascota.objects.all()
    tipos = TipoMascota.objects.all()
    razas = Razas.objects.all()

    tipo_edades = Mascota.CHOICES
    
    context = {
        'paises': paises,
        'provincias': provincias,
        'regiones': regiones,
        'comunas': comunas,
        'generos': generos,
        'estados': estados,
        'tipos': tipos,
        'razas': razas,
        'tipo_edades': tipo_edades 
    }
    
    # Mostrar el formulario de registro si el método es GET
    return render(request, 'registro_mascota.html', context)

@login_required(login_url="inicio_sesion")
def detalle_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    usuario_registrador = mascota.usuario  # Perfil del usuario que registró la mascota
    usuario_perfil = PerfilUsuario.objects.get(usuario_django=request.user)

    # Verificar si el usuario actual ya registró esta mascota
    es_registrador = (usuario_registrador == usuario_perfil)

    # Verificar si ya existe un formulario para esta mascota y este usuario
    formulario_existente = FormularioAdopcion.objects.filter(usuario=usuario_perfil, mascota=mascota).exists()
    
    context = {
        'mascota': mascota,
        'usuario_registrador': usuario_registrador,
        'formulario_existente': formulario_existente,
        'es_registrador': es_registrador,  # Pasamos esta información al template
    }

    return render(request, 'detalle_mascota.html', context)

def get_provincias(request, region_id):
    provincias = Provincia.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(provincias), safe=False)

def get_comunas(request, provincia_id):
    comunas = Comuna.objects.filter(provincia_id=provincia_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)

# Vista para obtener las provincias de una región de la mascota 
def get_provincias_mascota(request, region_id):
    provincias = ProvinciaMascota.objects.filter(region_id=region_id)
    data = [{"id": provincia.id, "nombre": provincia.nombre} for provincia in provincias]
    return JsonResponse(data, safe=False)

# Vista para obtener las comunas de una provincia de la mascota
def get_comunas_mascota(request, provincia_id):

    comunas = ComunaMascota.objects.filter(provincia_id=provincia_id)
    data = [{"id": comuna.id, "nombre": comuna.nombre} for comuna in comunas]
    return JsonResponse(data, safe=False)

@login_required(login_url="inicio_sesion")
def mascotas(request):
    try:
        # Obtiene el perfil del usuario actual utilizando el campo usuario_django
        perfil_usuario = PerfilUsuario.objects.get(usuario_django=request.user)
        # Filtra las mascotas asociadas a este perfil de usuario
        mascotas_usuario = Mascota.objects.filter(usuario=perfil_usuario)
    except PerfilUsuario.DoesNotExist:
        # Si el usuario no tiene un perfil asociado, se devuelve una lista vacía
        mascotas_usuario = []

    return render(request, "mis_mascotas.html", {"mascotas": mascotas_usuario})

@login_required(login_url="inicio_sesion")
def modificar_mascota(request, mascota_id):
    # Obtener la mascota, dirección y descripción
    mascota = get_object_or_404(Mascota, id=mascota_id)
    direccion = mascota.direccion
    descripcion_mascota = mascota.descripcion  # Referencia al modelo DescripcionMascota

    if request.method == 'POST':
        # Obtener los datos de la mascota desde el POST
        nombre = request.POST.get('nombre', mascota.nombre)
        apellido = request.POST.get('apellido', mascota.apellido)
        edad = request.POST.get('edad', mascota.edad)
        tipo_edad = request.POST.get('tipo_edad', mascota.tipo_edad)
        imagen = request.FILES.get('imagen', mascota.imagen)
        estado_mascota_id = request.POST.get('estado_mascota', mascota.estado_mascota.id)
        raza_id = request.POST.get('raza', mascota.raza.id)
        genero_id = request.POST.get('genero', mascota.genero.id)
        tipo_id = request.POST.get('tipo', mascota.tipo.id)
        
        # Obtener los datos de la dirección desde el POST
        calle = request.POST.get('calle', direccion.calle)
        numero = request.POST.get('numero', direccion.numero)
        comuna_id = request.POST.get('comuna', direccion.comuna.id)
        
        # Obtener los datos de descripción de la mascota desde el POST
        desc_fisica = request.POST.get('descripcion_fisica', descripcion_mascota.desc_fisica)
        desc_personalidad = request.POST.get('descripcion_personalidad', descripcion_mascota.desc_personalidad)
        desc_adicional = request.POST.get('descripcion_adicional', descripcion_mascota.desc_adicional)

        # Actualizar los atributos de la mascotaa
        mascota.nombre = nombre
        mascota.apellido = apellido
        mascota.edad = edad
        mascota.tipo_edad = tipo_edad
        mascota.imagen = imagen
        mascota.estado_mascota = EstadoMascota.objects.get(id=estado_mascota_id)
        mascota.raza = Razas.objects.get(id=raza_id)
        mascota.genero = GeneroMascota.objects.get(id=genero_id)
        mascota.tipo = TipoMascota.objects.get(id=tipo_id)
        mascota.save()  # Guardar los cambios de la mascota

        # Actualizar la dirección
        direccion.calle = calle
        direccion.numero = numero
        direccion.comuna = ComunaMascota.objects.get(id=comuna_id)
        direccion.save()  # Guardar los cambios de la dirección

        # Actualizar la descripción de la mascota
        descripcion_mascota.desc_fisica = desc_fisica
        descripcion_mascota.desc_personalidad = desc_personalidad
        descripcion_mascota.desc_adicional = desc_adicional
        descripcion_mascota.save()  # Guardar los cambios de la descripción

        # mensaje de éxito
        messages.success(request, 'La mascota ha sido modificada con éxito.', extra_tags='modificacion_mascota')

        # Redirigir a la lista de mascotas después de guardar
        return redirect('mascotas')

    # Obtener las opciones para los selectores
    estados = EstadoMascota.objects.all()
    razas = Razas.objects.all()
    generos = GeneroMascota.objects.all()
    tipos = TipoMascota.objects.all()
    regiones = RegionMascota.objects.all()
    provincias = ProvinciaMascota.objects.filter(region=direccion.comuna.provincia.region)
    comunas = ComunaMascota.objects.filter(provincia=direccion.comuna.provincia)

    context = {
        'mascota': mascota,
        'direccion': direccion,
        'descripcion_mascota': descripcion_mascota,
        'estados': estados,
        'razas': razas,
        'generos': generos,
        'tipos': tipos,
        'regiones': regiones,
        'provincias': provincias,
        'comunas': comunas,
    }

    return render(request, 'modificar_mascota.html', context)

def obtener_provincias(request, region_id):
    provincias = ProvinciaMascota.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(provincias), safe=False)

def obtener_comunas(request, provincia_id):
    comunas = ComunaMascota.objects.filter(provincia_id=provincia_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)

def eliminar_mascota(request, mascota_id):
    # Obtener la mascota que se desea eliminar
    mascota = get_object_or_404(Mascota, id=mascota_id)
    
    # Eliminar la mascota
    mascota.delete()

    # Redirigir a la lista de mascotas
    return redirect('mascotas')

@login_required(login_url="inicio_sesion")
def modificar_perfil(request):
    # Obtener el perfil del usuario logueado
    usuario_perfil = PerfilUsuario.objects.get(usuario_django=request.user)
    direccion = DireccionUsuario.objects.get(usuario=usuario_perfil)

    if request.method == "POST":
        # Campos editables
        telefono = request.POST.get("telefono")
        genero_id = request.POST.get("genero")
        comuna_id = request.POST.get("comuna")
        calle = request.POST.get("calle")
        numero = request.POST.get("numero")
        estado_economico_id = request.POST.get("estado_economico")
        email = request.POST.get("email")
        
        # Validar que el nuevo email no esté en uso por otro usuario
        if User.objects.filter(email=email).exclude(id=request.user.id).exists():
            messages.error(request, 'El correo electrónico ya está en uso. Por favor, elige otro.', extra_tags='correo_duplicado')
            return redirect("modificar_perfil")
        
        # Actualizar datos del usuario (User)
        request.user.email = email  # Actualizar el email
        request.user.username = email  # Actualizar el username como el email
        request.user.save()

        # Actualizar perfil de usuario
        usuario_perfil.telefono = telefono
        usuario_perfil.genero = Genero.objects.get(id=genero_id)
        usuario_perfil.estado_economico = EstadoEconomico.objects.get(id=estado_economico_id)
        usuario_perfil.save()
        
        

        # Actualizar dirección
        direccion.calle = calle
        direccion.numero = numero
        direccion.comuna = Comuna.objects.get(id=comuna_id)
        direccion.save()
        
        
        # mensaje de éxito
        messages.success(request, 'Sus datos han sido modificados con éxito.', extra_tags='modificacion_perfil')
        
        # Redirigir tras guardar cambios
        return redirect("perfil")

    # Cargar datos necesarios para el formulario
    generos = Genero.objects.all()
    regiones = Region.objects.all()
    estados_economicos = EstadoEconomico.objects.all() 
    provincias = Provincia.objects.filter(region=direccion.comuna.provincia.region)
    comunas = Comuna.objects.filter(provincia=direccion.comuna.provincia)
    
    context = {
        "usuario": request.user,
        "usuario_perfil": usuario_perfil,
        "direccion": direccion,
        "generos": generos,
        "regiones": regiones,
        "provincias": provincias,
        "comunas": comunas,
        "estados_economicos": estados_economicos,
    }

    return render(request, "modificar_perfil.html", context)

def obtener_provincias_perfil(request, region_id):
    provincias = Provincia.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(provincias), safe=False)

def obtener_comunas_perfil(request, provincia_id):
    comunas = Comuna.objects.filter(provincia_id=provincia_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)

@login_required(login_url="inicio_sesion")
def formulario_adopcion(request, mascota_id):
    
    mascota = get_object_or_404(Mascota, id=mascota_id)
    usuario_perfil = PerfilUsuario.objects.get(usuario_django=request.user)

    # Obtener dirección y los datos relacionados
    direccion = DireccionUsuario.objects.filter(usuario=usuario_perfil).select_related(
        'comuna__provincia__region__pais'
    ).first()

    # Datos relacionados
    comuna = direccion.comuna if direccion else None
    provincia = comuna.provincia if comuna else None
    region = provincia.region if provincia else None
    pais = region.pais if region else None

    # Verificar si ya existe un formulario para esta mascota y este usuario
    formulario_existente = FormularioAdopcion.objects.filter(usuario=usuario_perfil, mascota=mascota).exists()

    if formulario_existente:
        messages.warning(request, "Ya has enviado un formulario para adoptar esta mascota.")
        return redirect('detalle_mascota', mascota_id=mascota.id)

    if request.method == "POST":
        comentarios = request.POST.get("comentarios")
        estado_pendiente = EstadoFormulario.objects.get(descripcion="pendiente")

        # Crear el nuevo formulario de adopción
        formulario = FormularioAdopcion()
        formulario.comentarios = comentarios
        formulario.estado_formulario = estado_pendiente
        formulario.usuario = usuario_perfil
        formulario.mascota = mascota
        formulario.save()
        

        messages.success(request, "Tu formulario de adopción ha sido enviado exitosamente.")
        return redirect('detalle_mascota', mascota_id=mascota.id)

    context = {
        "usuario": request.user,
        "usuario_perfil": usuario_perfil,
        "mascota": mascota,
        "pais": pais,
        "region": region,
        "provincia": provincia,
        "comuna": comuna,
        "estado_economico": usuario_perfil.estado_economico
    }

    return render(request, "formulario_adopcion.html", context)

@login_required(login_url="inicio_sesion")
def mis_formularios(request):
    usuario = PerfilUsuario.objects.get(usuario_django=request.user)
    formularios = FormularioAdopcion.objects.filter(usuario=usuario)
    
    context = {
        'formularios' : formularios,
        'usuario' : usuario
    }
    
    return render(request, "mis_formularios.html", context)

@login_required(login_url="inicio_sesion")
def detalle_formulario(request, formulario_id):
    formulario = get_object_or_404(FormularioAdopcion, id=formulario_id)
    usuario = formulario.usuario
    direccion = DireccionUsuario.objects.filter(usuario=usuario).first()
    
    comuna = direccion.comuna if direccion else None
    provincia = comuna.provincia if comuna else None
    region = provincia.region if provincia else None
    pais = region.pais if region else None
    
    context = {
        
        'formulario' : formulario,
        'usuario' : usuario,
        'direccion' : direccion,
        'comuna': comuna,
        'provincia': provincia,
        'region': region,
        'pais': pais
                
    }
    
    return render(request, "detalle_formulario.html", context)

def eliminar_formulario(request, formulario_id):
    # Obtener la mascota que se desea eliminar
    formulario = get_object_or_404(FormularioAdopcion, id=formulario_id)
    
    # Eliminar la mascota
    formulario.delete()

    # Redirigir a la lista de mascotas
    return redirect('mis_formularios')

def actualizar_fundaciones(request):
    mensaje = consumir_y_guardar_fundaciones()
    return JsonResponse({"mensaje": mensaje})