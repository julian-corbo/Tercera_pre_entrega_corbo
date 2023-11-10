from django.contrib import admin
from django.urls import path

from blog.views import (
    CafeteriasCreateView,CafeteriasDeleteView,CafeteriasDetailView,CafeteriasListView,CafeteriasUpdateView,
    ArticulosCreateView,ArticulosDeleteView,ArticulosDetailView,ArticulosListView,ArticulosUpdateView,
    RecetasCreateView,RecetasDeleteView,RecetasDetailView,RecetasListView,RecetasUpdateView,
    buscar_cafeteria,buscar_articulo,buscar_receta,
)

urlpatterns = [
    #path('cafeterias/', lista_cafeterias, name='lista_cafeterias'),
    #path('recetas/', lista_recetas, name='lista_recetas'),
    #path('articulos/', lista_articulos, name='lista_articulos'),
    #path('crear-cafeteria/', crear_cafeteria, name='crear_cafeteria'),
    #path('crear-articulo/', crear_articulo, name='crear_articulo'),
    #path('crear-receta/', crear_receta, name='crear_receta'),

    #ListView
    path("cafeterias/", CafeteriasListView.as_view(), name="lista_cafeterias"),
    path("articulos/", ArticulosListView.as_view(), name="lista_articulos"),
    path("recetas/", RecetasListView.as_view(), name="lista_recetas"),

    #DetailView
    path('cafeterias/<int:pk>/', CafeteriasDetailView.as_view(), name="ver_cafeteria"),
    path('articulos/<int:pk>/', ArticulosDetailView.as_view(), name="ver_articulo"),
    path('recetas/<int:pk>/', RecetasDetailView.as_view(), name="ver_receta"),

    #CreateView
    path('crear-cafeteria/', CafeteriasCreateView.as_view(), name="crear_cafeteria"),
    path('crear-articulo/', ArticulosCreateView.as_view(), name="crear_articulo"),
    path('crear-receta/', RecetasCreateView.as_view(), name="crear_receta"),

    #UpdateView
    path('editar-cafeteria/<int:pk>/', CafeteriasUpdateView.as_view(), name="editar_cafeteria"),
    path('editar-articulo/<int:pk>/', ArticulosUpdateView.as_view(), name="editar_articulo"),
    path('editar-receta/<int:pk>/', RecetasUpdateView.as_view(), name="editar_receta"),


    #DeleteView
    path('eliminar-cafeteria/<int:pk>/', CafeteriasDeleteView.as_view(), name="eliminar_cafeteria"),
    path('eliminar-articulo/<int:pk>/', ArticulosDeleteView.as_view(), name="eliminar_articulo"),
    path('eliminar-receta/<int:pk>/', RecetasDeleteView.as_view(), name="eliminar_receta"),

    #Buscar
    path('buscar-cafeteria/', buscar_cafeteria, name='buscar_cafeteria'),
    path('buscar-articulo/', buscar_articulo, name= 'buscar_articulo'),
    path('buscar-receta/', buscar_receta, name='buscar_receta'),
    
]
