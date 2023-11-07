from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cafeterias(models.Model):
    nombre = models.CharField(max_length=64)
    direccion = models.CharField(max_length=1024)
    
class Recetas(models.Model):
    nombre = models.CharField(max_length=64)
    receta = models.TextField()

class Articulos(models.Model):
    autor = models.CharField(max_length=64)
    cafeteria_reseniada = models.ForeignKey(Cafeterias, on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=64)
    texto = models.TextField()
    puntaje = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
