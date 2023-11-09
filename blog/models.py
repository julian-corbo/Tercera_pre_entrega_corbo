from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cafeterias(models.Model):
    nombre = models.CharField(max_length=64)
    direccion = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.nombre}, Direccion: {self.direccion}'
    
class Recetas(models.Model):
    nombre = models.CharField(max_length=64)
    receta = models.TextField()

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    autor = models.CharField(max_length=64)
    cafeteria_reseniada = models.ForeignKey(Cafeterias, on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=64)
    texto = models.TextField()
    puntaje = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Escribe Sobre: {self.cafeteria_reseniada})" #me gustaria que solo me muestre el nombre y no la direccion
