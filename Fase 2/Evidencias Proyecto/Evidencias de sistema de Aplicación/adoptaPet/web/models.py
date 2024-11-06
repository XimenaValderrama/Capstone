from django.db import models
from django.contrib.auth.models import User


class EstadoEconomico(models.Model):
    
    descripcion = models.CharField(max_length=50, default="pendiente")

    def __str__(self):
        
        return self.descripcion

class Genero(models.Model):

    CHOICES = [
        ("masculino", "Masculino"),
        ("femenino", "Femenino"),
        ("prefiero_no_decir", "Prefiero no decir")
    ]
    descripcion = models.CharField(max_length=50, choices=CHOICES)

    def get_descripcion_display(self):

        return dict(self.CHOICES).get(self.descripcion, "Desconocido")

    def __str__(self):
        
        return self.descripcion

class PerfilUsuario(models.Model):

    rut = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    estado_economico = models.ForeignKey(EstadoEconomico, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    usuario_django = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.usuario_django.name

class Pais(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        
        return self.nombre

class Region(models.Model):
    
    nombre = models.CharField(max_length=60)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.nombre

class Provincia(models.Model):
    
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.nombre

class Comuna(models.Model):
    
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.nombre

class DireccionUsuario(models.Model):

    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        
        return self.calle


    
class EstadoMascota(models.Model):

    CHOICES = [
        ("pendiente", "Pendiente"),
        ("adoptado", "Adoptado"),
        ("en_adopcion", "En adopcion"),
        ("perdido", "Perdido"),
        ("encontrado", "Encontrado"),
    ]
    descripcion = models.CharField(max_length=50, choices=CHOICES, default="pendiente")

    def get_descripcion_display(self):

        return dict(self.CHOICES).get(self.descripcion, "Desconocido")

    def __str__(self):
        
        return self.descripcion
    
class Razas(models.Model):
    
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
            
        return self.nombre

class GeneroMascota(models.Model):

    CHOICES = [
        ("macho", "Macho"),
        ("hembra", "Hembra")
    ]
    descripcion = models.CharField(max_length=50, choices=CHOICES)

    def get_descripcion_display(self):

        return dict(self.CHOICES).get(self.descripcion, "Desconocido")

    def __str__(self):
        
        return self.descripcion
    
class DescripcionMascota(models.Model):

    desc_fisica = models.TextField()
    desc_personalidad = models.TextField()
    desc_adicional = models.TextField()

    def __str__(self):
        
        return str(self.id)
    
class TipoMascota(models.Model):

    descripcion = models.CharField(max_length=50)

    def __str__(self):
        
        return self.descripcion
    
class PaisMascota(models.Model):
    
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
            
        return self.nombre

class RegionMascota(models.Model):
    
    nombre = models.CharField(max_length=60)
    pais = models.ForeignKey(PaisMascota, on_delete=models.CASCADE)
    
    def __str__(self):
            
        return self.nombre
    
class ProvinciaMascota(models.Model):
    
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(RegionMascota, on_delete=models.CASCADE)
    
    def __str__(self):
            
        return self.nombre
    
class ComunaMascota(models.Model):
        
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(ProvinciaMascota, on_delete=models.CASCADE)
        
    def __str__(self):
                
        return self.nombre

class DireccionMascota(models.Model):
    
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comuna = models.ForeignKey(ComunaMascota, on_delete=models.CASCADE)
    
    def __str__(self):
            
        return self.calle

class Fundacion(models.Model):
    
    nombre = models.CharField(max_length=50)
    desc_fundacion = models.TextField()
    imagen = models.ImageField(upload_to="fundaciones/")
    url_fundacion = models.CharField(max_length=256)
    
    def __str__(self):
            
        return self.nombre

class Mascota(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to="mascotas/")
    estado_mascota = models.ForeignKey(EstadoMascota, on_delete=models.CASCADE)
    raza = models.ForeignKey(Razas, on_delete=models.CASCADE)
    genero = models.ForeignKey(GeneroMascota, on_delete=models.CASCADE)
    descripcion = models.ForeignKey(DescripcionMascota, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMascota, on_delete=models.CASCADE)
    direccion = models.ForeignKey(DireccionMascota, on_delete=models.CASCADE)
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.nombre


class EstadoFormulario(models.Model):

    CHOICES = [
        ("pendiente", "Pendiente"),
        ("aprobado", "Aprobado"),
        ("rechazado", "Rechazado")
    ]
    descripcion = models.CharField(max_length=50, choices=CHOICES, default="pendiente")

    def get_descripcion_display(self):

        return dict(self.CHOICES).get(self.descripcion, "Desconocido")

    def __str__(self):
        
        return self.descripcion

class FormularioAdopcion(models.Model):

    comentarios = models.TextField()
    estado_formulario = models.ForeignKey(EstadoFormulario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, null=True, blank=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        
        return self.mascota.nombre
    
class TipoAlimento(models.Model):
    
    tipo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        
        return self.tipo
    
class FichaMedica(models.Model):

    fecha_medica = models.DateField()
    prox_consulta = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    tipo_alimetno = models.ForeignKey(TipoAlimento, on_delete=models.CASCADE)

    def __str__(self):
        
        return str(self.id)

class Vacuna(models.Model):
    
    nombre = models.CharField(max_length=50)
    fecha_vacuna = models.DateField()
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    
    def __str__(self):
            
        return self.nombre
    
class Chip(models.Model):
    
    conf_chip = models.BooleanField(default="False")
    fecha_colocacion = models.DateField()
    lugar_colocacion = models.CharField(max_length=50)
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    
    def __str__(self):
            
        return self.conf_chip

class Desparasitacion(models.Model):
    
    conf_desparasitacion = models.BooleanField(default="False")
    fecha_desparasitacion = models.DateField()
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    
    def __str__(self):
            
        return str(self.id)
    
class Veterinaria(models.Model):
    
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)

    def __str__(self):
            
        return self.nombre

class TipoCirugia(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
            
        return self.nombre

class Cirugia(models.Model):

    descripcion = models.TextField()
    fecha_cirugia = models.DateField()
    tipo_cirugia = models.ForeignKey(TipoCirugia, on_delete=models.CASCADE)
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)

    def __str__(self):
            
        return self.descripcion
    
class Esterilizacion(models.Model):
    
    conf_esterilizacion = models.BooleanField(default="False")
    fecha_esterilizacion = models.DateField()
    lugar_esterilizacion = models.CharField(max_length=50)
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    
    def __str__(self):
            
        return self.conf_esterilizacion