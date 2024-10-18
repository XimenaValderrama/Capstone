from django.db import models
from django.contrib.auth.models import User


class EstadoEconomico(models.Model):
    
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

    def __str__(self):
        
        return self.calle

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

    def __str__(self):
        
        return str(self.id)

class PerfilUsuario(models.Model):

    rut = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    estado_economico = models.ForeignKey(EstadoEconomico, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    direccion_usuario = models.ForeignKey(DireccionUsuario, on_delete=models.CASCADE)
    usuario_django = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.usuario_django.name