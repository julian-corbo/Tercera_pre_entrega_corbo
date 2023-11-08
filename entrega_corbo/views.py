from django.shortcuts import render

def inicio(request):
    contexto= {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    
    return http_response
