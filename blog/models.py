from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Cafeterias(models.Model):
    nombre = models.CharField(max_length=64)
    direccion = models.CharField(max_length=1024)
    
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}'
    
class Recetas(models.Model):
    nombre = models.CharField(max_length=64)
    receta = models.TextField()

    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

from ckeditor.fields import RichTextField
class Articulos(models.Model):
    autor = models.CharField(max_length=64)
    cafeteria_reseniada = models.ForeignKey(Cafeterias, on_delete=models.CASCADE)

    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    titulo = models.CharField(max_length=64)
    texto = RichTextField()
    puntaje = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def save(self, *args, **kwargs):
        if self.creador:
            self.autor = f"{self.creador.first_name} {self.creador.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Escribe Sobre: {self.cafeteria_reseniada})" #me gustaria que solo me muestre el nombre y no la direccion
