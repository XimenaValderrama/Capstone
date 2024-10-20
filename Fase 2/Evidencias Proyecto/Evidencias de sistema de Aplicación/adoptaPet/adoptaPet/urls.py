
from django.contrib import admin
from django.urls import path
from web.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_sesion, name="inicio_sesion"),
    path('inicio/', inicio, name="inicio"),
    path('perfil/', perfil, name="perfil"),
    path('tenencia_responsable/', tenencia_responsable, name="tenencia_responsable"),
    path('adopcion/', adopcion, name="adopcion"),
    path('adoptados/', adoptados, name="adoptados"),
    path('busqueda/', busqueda, name="busqueda"),
    path('encontrados/', encontrados, name="encontrados"),
    path('registro/', registro, name="registro")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
