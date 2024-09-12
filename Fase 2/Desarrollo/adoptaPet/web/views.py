from django.shortcuts import render

# Create your views here.
def inicio(request):    

    return render(request, "index.html") 

def inicio_sesion(request):    

    return render(request, "login.html") 

def perfil(request):

    return render(request, "perfil.html")