from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarForm

#Vista Funcional
def signup(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('login')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/signup.html',
       context={'form': formulario},
   )

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
   )

def agregar_avatar(request):
  if request.method == "POST":
      formulario = AvatarForm(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

      if formulario.is_valid():
          avatar = formulario.save()
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('inicio')
          return redirect(url_exitosa)
  else:  # GET
      formulario = AvatarForm()
  return render(
      request=request,
      template_name="perfiles/avatar_form.html",
      context={'form': formulario},
  )


#Vista Basada en Clases
class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'perfiles/perfil_form.html'

   def get_object(self, queryset=None):
       return self.request.user

def about_me(request):
    
    context = {
        'nombre': 'Julian Corbo',
        'informacion': '''
            Soy estudiante de sociologia y me apasionan los metodos cuantitativos y los datos, por lo que me gustaria aprender mas de Data Science. 
            Para esto este curso de python fue el primer paso. Ademas, amo el cafe y actualmente soy barista asi que se me ocurrio que hacer un blog de reseñas
            de Montevideo era una idea divertida.
            ''',
        'foto_url': '/media/aboutme/julian.jfif',  
    }
    return render(request, 'perfiles/aboutme.html', context)