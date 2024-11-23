import requests
from django.core.management.base import BaseCommand
from web.models import Razas, TipoMascota

class Command(BaseCommand):
    help = "Carga las razas de perros y gatos desde sus respectivas APIs a la base de datos"

    def handle(self, *args, **kwargs):
        # URLs de las APIs
        dog_api_url = "https://api.thedogapi.com/v1/breeds"
        cat_api_url = "https://api.thecatapi.com/v1/breeds"

        # Obtén o crea los tipos de mascota
        tipo_perro, _ = TipoMascota.objects.get_or_create(descripcion="perro")
        tipo_gato, _ = TipoMascota.objects.get_or_create(descripcion="gato")

        # Cargar razas de perros
        self.cargar_razas(dog_api_url, tipo_perro, "perro")

        # Cargar razas de gatos
        self.cargar_razas(cat_api_url, tipo_gato, "gato")

    def cargar_razas(self, url, tipo_mascota, tipo_str):
        self.stdout.write(f"Cargando razas de {tipo_str} desde la API...")

        response = requests.get(url)

        if response.status_code == 200:
            breeds = response.json()
            for breed in breeds:
                # Crea o actualiza la raza en la base de datos
                Razas.objects.update_or_create(
                    nombre=breed["name"],
                    defaults={"tipo": tipo_mascota},
                )
            self.stdout.write(self.style.SUCCESS(f"¡Razas de {tipo_str} cargadas exitosamente!"))
        else:
            self.stdout.write(self.style.ERROR(f"Error al consumir la API de {tipo_str}: {response.status_code}"))
