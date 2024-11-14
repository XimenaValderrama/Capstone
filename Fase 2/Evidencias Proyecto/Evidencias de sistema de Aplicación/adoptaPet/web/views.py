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


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def modificar_eliminar_usuario(request, user_id):
    try:
        usuario = User.objects.get(id=user_id)
        perfil_usuario = PerfilUsuario.objects.get(usuario_django=usuario)
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
        perfil_usuario.delete()
        usuario.delete()
        return Response({"message": "Usuario y perfil eliminados correctamente."}, status=status.HTTP_204_NO_CONTENT)


@login_required(login_url="inicio_sesion")
def inicio(request):
    # Obtén todas las mascotas
    mascotas = Mascota.objects.all()
    
    # Pasa las mascotas al contexto del template
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
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
            return redirect('inicio_sesion')  # Redirigir de vuelta a la página de inicio de sesión

    # Si es una solicitud GET, mostrar el formulario de inicio de sesión
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
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro')

        # 3. Validar que el correo electrónico no exista
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
            return redirect('registro')

        # 4. Validar que el nombre de usuario (correo electrónico) no exista
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ya existe una cuenta con este correo electrónico.')
            return redirect('registro')

        # 5. Validar que el RUT no exista ya registrado en otro perfil de usuario
        if PerfilUsuario.objects.filter(rut=rut).exists():
            messages.error(request, 'El RUT ya está registrado.')
            return redirect('registro')

        # 6. Validar la longitud de la contraseña
        if len(password1) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return redirect('registro')

        # 7. Validar la longitud del telefono
        if not telefono.isdigit() or len(telefono) != 9:
            messages.error(request, 'El teléfono debe contener exactamente 9 dígitos. (Toma en cuenta el 9 del incio)')
            return redirect('registro')

        # Validar la longitud del RUT (8 o 9 dígitos)
        if not rut_numerico.isdigit() or not (8 <= len(rut_numerico) <= 9):
            messages.error(request, 'El RUT debe contener 8 o 9 dígitos sin puntos ni guion.')
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

        return redirect('inicio_sesion')
    else:
        # 12. Mostrar el formulario de registro
        return render(request, 'registro.html', context)

@login_required(login_url="inicio_sesion")
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion') 

@login_required(login_url="inicio_sesion")
def registro_mascota(request):
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

        # Crear la instancia de DescripcionMascota
        descripcion = DescripcionMascota.objects.create(
            desc_fisica=desc_fisica,
            desc_personalidad=desc_personalidad,
            desc_adicional=desc_adicional
        )

        # Validar y obtener instancias de relaciones ForeignKey
        estado_mascota = EstadoMascota.objects.get(id=estado_mascota_id)
        raza = Razas.objects.get(id=raza_id)
        genero = GeneroMascota.objects.get(id=genero_id)
        tipo = TipoMascota.objects.get(id=tipo_id)
        comuna = ComunaMascota.objects.get(id=comuna_id)
        usuario = PerfilUsuario.objects.get(usuario_django=request.user)

        # Crear la nueva dirección para la mascota
        direccion = DireccionMascota.objects.create(
            calle=calle,
            numero=numero,
            comuna=comuna
        )

        # Crear la nueva mascota asociada con la descripción, dirección, y tipo de edad
        mascota = Mascota.objects.create(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            tipo_edad=tipo_edad,  # <-- Asigna el tipo de edad aquí
            imagen=imagen,
            estado_mascota=estado_mascota,
            raza=raza,
            genero=genero,
            descripcion=descripcion,
            tipo=tipo,
            direccion=direccion,  # Asocia la dirección recién creada
            usuario=usuario
        )

        # Redirigir a otra página después de guardar
        return redirect('inicio')  # Cambia 'login' a la URL a la que quieres redirigir después del registro

    # Mostrar el formulario de registro si el método es GET
    return render(request, 'registro_mascota.html', context)

@login_required(login_url="inicio_sesion")
def detalle_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    usuario_registrador = mascota.usuario  # Obtenemos el perfil del usuario que registró la mascota
    return render(request, 'detalle_mascota.html', {'mascota': mascota, 'usuario_registrador': usuario_registrador})

def get_provincias(request, region_id):
    provincias = Provincia.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(provincias), safe=False)

def get_comunas(request, provincia_id):
    comunas = Comuna.objects.filter(provincia_id=provincia_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)

# Vista para obtener las provincias de una región
def get_provincias_mascota(request, region_id):
    provincias = ProvinciaMascota.objects.filter(region_id=region_id)
    data = [{"id": provincia.id, "nombre": provincia.nombre} for provincia in provincias]
    return JsonResponse(data, safe=False)

# Vista para obtener las comunas de una provincia
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

        # Actualizar los atributos de la mascota
        mascota.nombre = nombre
        mascota.apellido = apellido
        mascota.edad = edad
        mascota.tipo_edad = tipo_edad
        mascota.imagen = imagen
        mascota.estado_mascota_id = estado_mascota_id
        mascota.raza_id = raza_id
        mascota.genero_id = genero_id
        mascota.tipo_id = tipo_id
        mascota.save()  # Guardar los cambios de la mascota

        # Actualizar la dirección
        direccion.calle = calle
        direccion.numero = numero
        direccion.comuna_id = comuna_id
        direccion.save()  # Guardar los cambios de la dirección

        # Actualizar la descripción de la mascota
        descripcion_mascota.desc_fisica = desc_fisica
        descripcion_mascota.desc_personalidad = desc_personalidad
        descripcion_mascota.desc_adicional = desc_adicional
        descripcion_mascota.save()  # Guardar los cambios de la descripción

        # mensaje de éxito
        messages.success(request, 'La mascota ha sido modificada con éxito.')

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
