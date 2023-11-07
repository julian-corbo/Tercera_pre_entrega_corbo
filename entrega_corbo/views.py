from django.shortcuts import render

def lista_cafeterias(request):

    http_response = render(
        request=request,
        template_name='base.html',
    )
    
    return http_response
