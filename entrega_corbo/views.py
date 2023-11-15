from django.shortcuts import render
from blog.models import Articulos

def inicio(request):
    articulos = Articulos.objects.all()[:3]

    contexto= {"articulos":articulos}

    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    
    return http_response
