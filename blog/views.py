from django.shortcuts import render

from blog.models import Cafeterias,Recetas,Articulos

def lista_cafeterias(request):

    contexto = {
        'cafeterias':Cafeterias.objects.all()
    }

    http_response = render(
        request=request,
        template_name='blog/cafeterias.html',
        context=contexto,
    )
    
    return http_response


def lista_recetas(request):

    contexto = {
        'recetas':Recetas.objects.all()
    }

    http_response = render(
        request=request,
        template_name='blog/recetas.html',
        context=contexto,
    )
    
    return http_response

def lista_articulos(request):

    contexto = {
        'articulos':Articulos.objects.all()
    }

    http_response = render(
        request=request,
        template_name='blog/articulos.html',
        context=contexto,
    )
    
    return http_response
