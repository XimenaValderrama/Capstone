from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Selecciona solo los campos necesarios
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }

class EstadoEconomicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEconomico
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    estado_economico = EstadoEconomicoSerializer()
    genero = GeneroSerializer()
    usuario_django = UserSerializer()

    class Meta:
        model = PerfilUsuario
        fields = '__all__'

    def update(self, instance, validated_data):
        # Actualizar estado_economico
        estado_economico_data = validated_data.pop('estado_economico', None)
        if estado_economico_data:
            for attr, value in estado_economico_data.items():
                setattr(instance.estado_economico, attr, value)
            instance.estado_economico.save()


        # Actualizar usuario_django
        usuario_django_data = validated_data.pop('usuario_django', None)
        if usuario_django_data:
            for attr, value in usuario_django_data.items():
                setattr(instance.usuario_django, attr, value)
            instance.usuario_django.save()

        # Actualizar los campos restantes del PerfilUsuario
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):

    pais = PaisSerializer()

    class Meta:
        model = Region
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):

    region = RegionSerializer()

    class Meta:
        model = Provincia
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):

    provincia = ProvinciaSerializer()

    class Meta:
        model = Comuna
        fields = '__all__'

class DireccionUsuarioSerializer(serializers.ModelSerializer):

    comuna = ComunaSerializer()
    usuario = PerfilUsuarioSerializer()

    class Meta:
        model = DireccionUsuario
        fields = '__all__'

class EstadoMascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadoMascota
        fields = '__all__'

class RazasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Razas
        fields = '__all__'

class GeneroMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroMascota
        fields = '__all__'

class DescripcionMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  DescripcionMascota
        fields = '__all__'

class TipoMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMascota
        fields = '__all__'

class PaisMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaisMascota
        fields = '__all__'

class RegionMascotaSerializer(serializers.ModelSerializer):

    pais = PaisMascotaSerializer()

    class Meta:
        model = RegionMascota
        fields = '__all__'

class ProvinciaMascotaSerializer(serializers.ModelSerializer):

    region = RegionMascotaSerializer()

    class Meta:
        model = ProvinciaMascota
        fields = '__all__'

class ComunaMascotaSerializer(serializers.ModelSerializer):

    provincia = ProvinciaMascotaSerializer()

    class Meta:
        model = ComunaMascota
        fields = '__all__'

class DireccionMascotaSerializer(serializers.ModelSerializer):

    comuna = ComunaMascotaSerializer()


    class Meta:
        model = DireccionMascota
        fields = '__all__'

class FundacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundacion
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):

    #Definimos los serializadores de las relaciones para que se muestren con sus nombres y no solo id en el JSON
    estado_mascota = EstadoMascotaSerializer()
    raza = RazasSerializer()
    genero = GeneroMascotaSerializer()
    descripcion = DescripcionMascotaSerializer()
    tipo = TipoMascotaSerializer()
    direccion = DireccionMascotaSerializer()
    usuario = PerfilUsuarioSerializer()
    fundacion = FundacionSerializer()

    class Meta:
        model = Mascota
        fields = '__all__'

class EstadoFormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoFormulario
        fields = '__all__'

class FormularioAdopcionSerializer(serializers.ModelSerializer):

    estado_formulario = EstadoFormularioSerializer()
    mascota = MascotaSerializer()
    usuario = PerfilUsuarioSerializer()

    class Meta:
        model = FormularioAdopcion
        fields = '__all__'

class TipoAlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAlimento
        fields = '__all__'

class FichaMedicaSerializer(serializers.ModelSerializer):

    mascota = MascotaSerializer()
    tipo_alimento = TipoAlimentoSerializer()

    class Meta:
        model = FichaMedica
        fields = '__all__'

class VacunaSerializer(serializers.ModelSerializer):

    ficha_medica = FichaMedicaSerializer()

    class Meta:
        model = Vacuna
        fields = '__all__'

class ChipSerializer(serializers.ModelSerializer):

    ficha_medica = FichaMedicaSerializer()

    class Meta:
        model = Chip
        fields = '__all__'

class DesparasitacionSerializer(serializers.ModelSerializer):

    ficha_medica = FichaMedicaSerializer()

    class Meta:
        model = Desparasitacion
        fields = '__all__'

class VeterinariaSerializer(serializers.ModelSerializer):

    ficha_medica = FichaMedicaSerializer()

    class Meta:
        model = Veterinaria
        fields = '__all__'

class TipoCirugiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCirugia
        fields = '__all__'

class CirugiaSerializer(serializers.ModelSerializer):

    tipo_cirugia = TipoCirugiaSerializer()
    ficha_medica = FichaMedicaSerializer()

    class Meta:
        model = Cirugia
        fields = '__all__'

class EsterilizacionSerializer(serializers.ModelSerializer):

    ficha_medica = FichaMedicaSerializer()

    class Meta:
        model = Esterilizacion
        fields = '__all__'
