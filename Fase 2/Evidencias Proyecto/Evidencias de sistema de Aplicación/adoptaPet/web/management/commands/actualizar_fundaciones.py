from django.core.management.base import BaseCommand
from web.cargar_datos_fundaciones import consumir_y_guardar_fundaciones

class Command(BaseCommand):
    help = "Actualiza la base de datos con las fundaciones obtenidas de la API de Huachitos"

    def handle(self, *args, **kwargs):
        mensaje = consumir_y_guardar_fundaciones()
        self.stdout.write(self.style.SUCCESS(mensaje))