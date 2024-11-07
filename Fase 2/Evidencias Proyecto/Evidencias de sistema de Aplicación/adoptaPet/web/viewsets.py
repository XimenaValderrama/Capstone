from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import IsSuperAdmin
from rest_framework.permissions import IsAuthenticated

class EstadoEconomicoViewSet(viewsets.ModelViewSet):
    queryset = EstadoEconomico.objects.all()
    serializer_class = EstadoEconomicoSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated]

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [IsAuthenticated]

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = [IsAuthenticated]

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    permission_classes = [IsAuthenticated]

class DireccionUsuarioViewSet(viewsets.ModelViewSet):
    queryset = DireccionUsuario.objects.all()
    serializer_class = DireccionUsuarioSerializer
    permission_classes = [IsAuthenticated]

class EstadoMascotaViewSet(viewsets.ModelViewSet):
    queryset = EstadoMascota.objects.all()
    serializer_class = EstadoMascotaSerializer
    permission_classes = [IsAuthenticated]

class RazasViewSet(viewsets.ModelViewSet):
    queryset = Razas.objects.all()
    serializer_class = RazasSerializer
    permission_classes = [IsAuthenticated]

class GeneroMascotaViewSet(viewsets.ModelViewSet):
    queryset = GeneroMascota.objects.all()
    serializer_class = GeneroMascotaSerializer
    permission_classes = [IsAuthenticated]

class DescripcionMascotaViewSet(viewsets.ModelViewSet):
    queryset = DescripcionMascota.objects.all()
    serializer_class = DescripcionMascotaSerializer
    permission_classes = [IsAuthenticated]

class TipoMascotaViewSet(viewsets.ModelViewSet):
    queryset = TipoMascota.objects.all()
    serializer_class = TipoMascotaSerializer
    permission_classes = [IsAuthenticated]

class PaisMascotaViewSet(viewsets.ModelViewSet):
    queryset = PaisMascota.objects.all()
    serializer_class = PaisMascotaSerializer
    permission_classes = [IsAuthenticated]

class RegionMascotaViewSet(viewsets.ModelViewSet):  
    queryset = RegionMascota.objects.all()
    serializer_class = RegionMascotaSerializer
    permission_classes = [IsAuthenticated]

class ProvinciaMascotaViewSet(viewsets.ModelViewSet):
    queryset = ProvinciaMascota.objects.all()
    serializer_class = ProvinciaMascotaSerializer
    permission_classes = [IsAuthenticated]

class ComunaMascotaViewSet(viewsets.ModelViewSet):
    queryset = ComunaMascota.objects.all()
    serializer_class = ComunaMascotaSerializer
    permission_classes = [IsAuthenticated]

class DireccionMascotaViewSet(viewsets.ModelViewSet):
    queryset = DireccionMascota.objects.all()
    serializer_class = DireccionMascotaSerializer
    permission_classes = [IsAuthenticated]

class FundacionViewSet(viewsets.ModelViewSet):
    queryset = Fundacion.objects.all()
    serializer_class = FundacionSerializer
    permission_classes = [IsAuthenticated]

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [IsAuthenticated]

class EstadoFormularioViewSet(viewsets.ModelViewSet):
    queryset = EstadoFormulario.objects.all()
    serializer_class = EstadoFormularioSerializer
    permission_classes = [IsAuthenticated]

class FormularioAdopcionViewSet(viewsets.ModelViewSet):
    queryset = FormularioAdopcion.objects.all()
    serializer_class = FormularioAdopcionSerializer
    permission_classes = [IsAuthenticated]

class TipoAlimentoViewSet(viewsets.ModelViewSet):
    queryset = TipoAlimento.objects.all()
    serializer_class = TipoAlimentoSerializer
    permission_classes = [IsAuthenticated]

class FichaMedicaViewSet(viewsets.ModelViewSet):
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer
    permission_classes = [IsAuthenticated]

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer
    permission_classes = [IsAuthenticated]

class ChipViewSet(viewsets.ModelViewSet):
    queryset = Chip.objects.all()
    serializer_class = ChipSerializer
    permission_classes = [IsAuthenticated]

class DesparasitacionViewSet(viewsets.ModelViewSet):
    queryset = Desparasitacion.objects.all()
    serializer_class = DesparasitacionSerializer
    permission_classes = [IsAuthenticated]

class VeterinariaViewSet(viewsets.ModelViewSet):
    queryset = Veterinaria.objects.all()
    serializer_class = VeterinariaSerializer
    permission_classes = [IsAuthenticated]

class TipoCirugiaViewSet(viewsets.ModelViewSet):
    queryset = TipoCirugia.objects.all()
    serializer_class = TipoCirugiaSerializer
    permission_classes = [IsAuthenticated]

class CirugiaViewSet(viewsets.ModelViewSet):
    queryset = Cirugia.objects.all()
    serializer_class = CirugiaSerializer
    permission_classes = [IsAuthenticated]

class EsterilizacionViewSet(viewsets.ModelViewSet):
    queryset = Esterilizacion.objects.all()
    serializer_class = EsterilizacionSerializer
    permission_classes = [IsAuthenticated]

