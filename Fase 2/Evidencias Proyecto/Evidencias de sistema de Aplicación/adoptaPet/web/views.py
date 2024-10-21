from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="inicio_sesion")
def inicio(request):    

    return render(request, "index.html") 

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

    return render(request, "perfil.html")

@login_required(login_url="inicio_sesion")
def tenencia_responsable(request):

    return render(request, "tenencia_responsable.html")

@login_required(login_url="inicio_sesion")
def adopcion(request):

    return render(request, "adopcion.html")

@login_required(login_url="inicio_sesion")
def adoptados(request):

    return render(request, "adoptados.html")

@login_required(login_url="inicio_sesion")
def busqueda(request):

    return render(request, "busqueda.html")

@login_required(login_url="inicio_sesion")
def encontrados(request):

    return render(request, "encontrados.html")


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

        # 5. Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=nombre, last_name=apellido)
        user.save()
        perfilusuario = PerfilUsuario()
        perfilusuario.usuario_django = user
        perfilusuario.rut = rut
        perfilusuario.telefono = telefono
        perfilusuario.genero = Genero.objects.get(id=genero)
        perfilusuario.estado_economico = EstadoEconomico.objects.get(id=estado_economico)
        perfilusuario.save()

        direccionusuario = DireccionUsuario()
        direccionusuario.calle = calle
        direccionusuario.numero = numero
        direccionusuario.comuna = Comuna.objects.get(id=comuna)
        direccionusuario.save()
        
        return redirect('inicio_sesion')
    else:
        # 7. Mostrar el formulario de registro
        return render(request, 'registro.html', context)

@login_required(login_url="inicio_sesion")
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion') 