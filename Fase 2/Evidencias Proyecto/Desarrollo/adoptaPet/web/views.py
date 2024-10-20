from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def inicio(request):    

    return render(request, "index.html") 

def inicio_sesion(request):    

    return render(request, "login.html") 

def perfil(request):

    return render(request, "perfil.html")


def tenencia_responsable(request):

    return render(request, "tenencia_responsable.html")

def adopcion(request):

    return render(request, "adopcion.html")

def adoptados(request):

    return render(request, "adoptados.html")

def busqueda(request):

    return render(request, "busqueda.html")

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
        provincia = request.POST['provincia']
        region = request.POST['region']
        pais = request.POST['pais']
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
        
        # 6. Autenticar y iniciar sesión
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, 'Registro exitoso y sesión iniciada.')
            return redirect('inicio')  # Redirige a la página principal
        else:
            messages.error(request, 'Hubo un error al iniciar sesión.')
            return redirect('login')
    else:
        # 7. Mostrar el formulario de registro
        return render(request, 'registro.html', context)