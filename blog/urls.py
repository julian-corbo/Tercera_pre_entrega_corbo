from django.contrib import admin
from django.urls import path

from blog.views import (
    lista_articulos,lista_cafeterias,lista_recetas,crear_articulo,crear_cafeteria,crear_receta,buscar_cafeteria,buscar_receta,buscar_articulo
)

urlpatterns = [
    path('cafeterias/', lista_cafeterias, name='lista_cafeterias'),
    path('recetas/', lista_recetas, name='lista_recetas'),
    path('articulos/', lista_articulos, name='lista_articulos'),
    path('crear-cafeteria/', crear_cafeteria, name='crear_cafeteria'),
    path('crear-articulo/', crear_articulo, name='crear_articulo'),
    path('crear-receta/', crear_receta, name='crear_receta'),
    path('buscar-cafeteria/', buscar_cafeteria, name='buscar_cafeteria'),
    path('buscar-receta/', buscar_receta, name='buscar_receta'),
    path('buscar-articulo/', buscar_articulo, name= 'buscar_articulo'),
    
]
