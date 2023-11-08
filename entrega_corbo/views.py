from django.shortcuts import render

def inicio(request):

    http_response = render(
        request=request,
        template_name='inicio.html',
    )
    
    return http_response
