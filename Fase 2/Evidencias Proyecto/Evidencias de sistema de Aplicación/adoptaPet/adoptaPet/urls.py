
from django.contrib import admin
from django.urls import path, include
from web.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from web.viewsets import *
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'estadoeconomico', EstadoEconomicoViewSet)
router.register(r'genero', GeneroViewSet)
router.register(r'perfilusuario', PerfilUsuarioViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'region', RegionViewSet)
router.register(r'provincia', ProvinciaViewSet)
router.register(r'comuna', ComunaViewSet)
router.register(r'direccionusuario', DireccionUsuarioViewSet)
router.register(r'estadomascota', EstadoMascotaViewSet)
router.register(r'razas', RazasViewSet)
router.register(r'generomascota', GeneroMascotaViewSet)
router.register(r'descripcionmascota', DescripcionMascotaViewSet)
router.register(r'tipomascota', TipoMascotaViewSet)
router.register(r'paismascota', PaisMascotaViewSet)
router.register(r'regionmascota', RegionMascotaViewSet)
router.register(r'provinciamascota', ProvinciaMascotaViewSet)
router.register(r'comunamascota', ComunaMascotaViewSet)
router.register(r'direccionmascota', DireccionMascotaViewSet)
router.register(r'fundacion', FundacionViewSet)
router.register(r'mascota', MascotaViewSet)
router.register(r'estadoformulario', EstadoFormularioViewSet)
router.register(r'formulario', FormularioAdopcionViewSet)
router.register(r'tipoalimento', TipoAlimentoViewSet)
router.register(r'fichamedica', FichaMedicaViewSet)
router.register(r'vacuna', VacunaViewSet)
router.register(r'chip', ChipViewSet)
router.register(r'desparasitacion', DesparasitacionViewSet)
router.register(r'veterinaria', VeterinariaViewSet)
router.register(r'tipocirugia', TipoCirugiaViewSet)
router.register(r'cirugia', CirugiaViewSet)
router.register(r'esterilizacion', EsterilizacionViewSet)

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
    path('registro/', registro, name="registro"),
    path('registro_mascota/', registro_mascota, name="registro_mascota"),
    path('mascotas/', mascotas, name="mascotas"),
    path('detalle_mascota/<int:mascota_id>/', detalle_mascota, name='detalle_mascota'),
    path('cerrar-sesion', cerrar_sesion, name="cerrar_sesion"),
    path('get_provincias/<int:region_id>/', get_provincias, name='get_provincias'),
    path('get_comunas/<int:provincia_id>/', get_comunas, name='get_comunas'),
    path('api/', include(router.urls)),
    path('api/token/', views.obtain_auth_token, name='api_token_auth'),
    path('usuario/<int:user_id>/', modificar_eliminar_usuario, name='modificar_eliminar_usuario'),
    path('get_provincias_mascota/<int:region_id>/', get_provincias_mascota, name='get_provincias_mascota'),
    path('get_comunas_mascota/<int:provincia_id>/', get_comunas_mascota, name='get_comunas_mascota'),
    path('modificar_mascota/<int:mascota_id>/', modificar_mascota, name='modificar_mascota'),
    path('ajax/provincias/<int:region_id>/', obtener_provincias, name='obtener_provincias'),
    path('ajax/comunas/<int:provincia_id>/', obtener_comunas, name='obtener_comunas'),
    path('eliminar_mascota/<int:mascota_id>/', eliminar_mascota, name='eliminar_mascota'),
    path('modificar_perfil/', modificar_perfil, name="modificar_perfil"),
    path('get_provincias/<int:region_id>/', obtener_provincias_perfil, name='get_provincias'),
    path('get_comunas/<int:provincia_id>/', obtener_comunas_perfil, name='get_comunas'),
    path('formulario_adopcion/<int:mascota_id>/', formulario_adopcion, name='formulario_adopcion'),
    path('eliminar_usuario/<int:user_profile_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('mis_formularios/', mis_formularios, name="mis_formularios"),
    path('detalle_formulario/<int:formulario_id>/', detalle_formulario, name="detalle_formulario"),
    path('eliminar_formulario/<int:formulario_id>/', eliminar_formulario, name='eliminar_formulario'),
    path('actualizar-fundaciones/', actualizar_fundaciones, name='actualizar_fundaciones'),
    path('fundaciones/', fundaciones, name='fundaciones'),
    path('detalle_fundacion/<int:fundacion_id>/', detalle_fundacion, name="detalle_fundacion"),
    path('mascota/<int:mascota_id>/ficha_medica/', ficha_medica, name='ficha_medica'),
    path('formularios_mascota/<int:mascota_id>/', formularios_mascota, name='formularios_mascota'),
    path('eliminar_formulario_solicitante/<int:formulario_id>/', eliminar_formulario_solicitante, name='eliminar_formulario_solicitante'),
    path('cambiar_estado_formulario/<int:formulario_id>/', cambiar_estado_formulario, name='cambiar_estado_formulario'),
    path('detalle_ficha_medica/<int:ficha_id>/', detalle_ficha_medica, name='detalle_ficha_medica'),
    path('eliminar_ficha_medica/<int:ficha_medica_id>/', eliminar_ficha_medica, name='eliminar_ficha_medica'),
    path('mascotas/<int:mascota_id>/', modificar_eliminar_mascota, name='modificar_eliminar_mascota'),
    path('mascotas/<int:mascota_id>/estado/', actualizar_estado_mascota, name='actualizar_estado_mascota'),
    path('formularios/<int:formulario_id>/estado/', actualizar_estado_formulario, name='actualizar_estado_formulario'),
    path('formulario/<int:formulario_id>/', modificar_eliminar_formulario, name='modificar_eliminar_formulario'),
    path('modificar_ficha_medica-adopcion/<int:ficha_medica_id>/', modificar_ficha_medica, name='modificar_ficha_medica'),
    path('fundacion/<int:fundacion_id>/', modificar_eliminar_fundacion, name='modificar_eliminar_fundacion'),
    path('get_razas/<str:tipo_id>/', get_razas, name='get_razas'),
    path('detalle_ficha_medica_masc/<int:ficha_id>/', detalle_ficha_medica_masc, name='detalle_ficha_medica_masc'),
    path('obtener_razas/<int:tipo_id>/', obtener_razas, name='obtener_razas'),
    path('ficha_medica/<int:ficha_medica_id>/', modificar_eliminar_ficha_medica, name='modificar_eliminar_ficha_medica'),
    path('perfiles/<int:perfil_id>/estado-economico/', actualizar_estado_economico, name='actualizar_estado_economico'),
    path('perfiles/<int:perfil_id>/genero/', actualizar_genero, name='actualizar_genero'),


 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
