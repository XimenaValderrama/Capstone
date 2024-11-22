import requests
from .models import Fundacion
from django.core.files.base import ContentFile


def consumir_y_guardar_fundaciones():
    
    url = "https://huachitos.cl/api/equipos"  # Endpoint real para las fundaciones
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            for item in datos['data']:
                # Obtener y validar la descripción
                descripcion = item.get("descripcion", "")
                if descripcion is None or descripcion.strip() == "":
                    descripcion = "Descripción no disponible"

                # Crear o actualizar la fundación sin guardar aún
                fundacion, created = Fundacion.objects.update_or_create(
                    nombre=item["nombre"],  # Campo del modelo
                    defaults={
                        "desc_fundacion": descripcion,  # Valor siempre seguro
                        "url_fundacion": item.get("url", ""),  # Valor de URL o vacío
                    },
                )

                # Descargar y guardar la imagen localmente si está disponible
                imagen_url = item.get("imagen", "")
                if imagen_url:
                    try:
                        imagen_response = requests.get(imagen_url)
                        if imagen_response.status_code == 200:
                            # Guardar la imagen en el campo del modelo
                            fundacion.imagen.save(
                                f"{fundacion.nombre.replace(' ', '_').lower()}.jpg",  # Nombre de archivo
                                ContentFile(imagen_response.content),  # Contenido de la imagen
                                save=True,
                            )
                    except requests.exceptions.RequestException:
                        print(f"Error al descargar la imagen para la fundación: {fundacion.nombre}")

            return "Fundaciones insertadas o actualizadas correctamente."
        else:
            return f"Error en la API: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con la API: {e}"