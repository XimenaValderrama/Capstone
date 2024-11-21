import requests
from .models import Fundacion

def consumir_y_guardar_fundaciones():
    import requests
    from .models import Fundacion
    
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
                
                Fundacion.objects.update_or_create(
                    nombre=item["nombre"],  # Campo del modelo
                    defaults={
                        "desc_fundacion": descripcion,  # Valor siempre seguro
                        "imagen": item.get("imagen", ""),  # Valor de imagen o vacío
                        "url_fundacion": item.get("url", ""),  # Valor de URL o vacío
                    },
                )
            return "Fundaciones insertadas o actualizadas correctamente."
        else:
            return f"Error en la API: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con la API: {e}"
