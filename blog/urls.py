from django.contrib import admin
from django.urls import path

from blog.views import lista_articulos,lista_cafeterias,lista_recetas

urlpatterns = [
    path('cafeterias/', lista_cafeterias, name='lista_cafeterias'),
    path('recetas/', lista_recetas, name='lista_recetas'),
    path('articulos/', lista_articulos, name='lista_articulos'),
]
