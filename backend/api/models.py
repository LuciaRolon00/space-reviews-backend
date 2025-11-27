from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, blank=True, null=True) 
    plataforma = models.CharField(max_length=100, blank=True, null=True)
    desarrollador = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.URLField(max_length=255, blank=True, null=True)
    estrellas = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.motivo}"