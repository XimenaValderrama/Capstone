
from django.contrib import admin
from django.urls import path
from web.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('inicio_sesion', inicio_sesion, name="inicio_sesion")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
