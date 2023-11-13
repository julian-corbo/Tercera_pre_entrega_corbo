from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import CafeteriaFormulario,ArticulosFormulario,RecetasFormulario
from blog.models import Cafeterias,Recetas,Articulos



#ListView
class CafeteriasListView(ListView):
   model = Cafeterias
   template_name = 'blog/lista_cafeterias.html'

class ArticulosListView(ListView):
   model = Articulos
   template_name = 'blog/lista_articulos.html'

class RecetasListView(ListView):
   model = Recetas
   template_name = 'blog/lista_recetas.html'

#DetailView

class CafeteriasDetailView(DetailView):
   model = Cafeterias
   success_url = reverse_lazy('lista_cafeterias')
   
class ArticulosDetailView(DetailView):
   model = Articulos
   success_url = reverse_lazy('lista_articulos')

class RecetasDetailView(DetailView):
   model = Recetas
   success_url = reverse_lazy('lista_recetas')

#CreateView

class CafeteriasCreateView(LoginRequiredMixin,CreateView):
   model = Cafeterias
   fields = ('nombre', 'direccion')
   success_url = reverse_lazy('lista_cafeterias')

   def form_valid(self, form):
    """If the form is valid, save the associated model."""
    self.object = form.save(creador= self.request.user)
    return super().form_valid(form)
   
class ArticulosCreateView(LoginRequiredMixin,CreateView):
   model = Articulos
   fields = ('autor', 'cafeteria_reseniada','titulo','texto','puntaje')
   success_url = reverse_lazy('lista_articulos')
   
   def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.creador = self.request.user
        return super().form_valid(form)
   
class RecetasCreateView(LoginRequiredMixin,CreateView):
   model = Recetas
   fields = ('nombre', 'receta')
   success_url = reverse_lazy('lista_recetas')
   
   def form_valid(self, form):
    self.object = form.save(creador= self.request.user)
    return super().form_valid(form)

   

#UpdateView
class CafeteriasUpdateView(LoginRequiredMixin,UpdateView):
   model = Cafeterias
   fields = ('nombre', 'direccion')
   success_url = reverse_lazy('lista_cafeterias')

class ArticulosUpdateView(LoginRequiredMixin,UpdateView):
   model = Articulos
   fields = ('autor', 'cafeteria_reseniada','titulo','texto','puntaje')
   success_url = reverse_lazy('lista_articulos')

class RecetasUpdateView(LoginRequiredMixin,UpdateView):
   model = Recetas
   fields = ('nombre', 'receta')
   success_url = reverse_lazy('lista_recetas')

#DeleteView

class CafeteriasDeleteView(LoginRequiredMixin,DeleteView):
   model = Cafeterias
   success_url = reverse_lazy('lista_cafeterias')

class ArticulosDeleteView(LoginRequiredMixin,DeleteView):
   model = Articulos
   success_url = reverse_lazy('lista_articulos')

class RecetasDeleteView(LoginRequiredMixin,DeleteView):
   model = Recetas
   success_url = reverse_lazy('lista_recetas')

#Vista Funcional
#Buscar
def buscar_cafeteria(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       cafeteria = Cafeterias.objects.filter(nombre__icontains=busqueda)
       contexto = {
           "cafeterias": cafeteria,
       }
       http_response = render(
           request=request,
           template_name='blog/cafeterias.html',
           context=contexto,
       )
       return http_response

def buscar_receta(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       receta = Recetas.objects.filter(nombre__icontains=busqueda)
       contexto = {
           "recetas": receta,
       }
       http_response = render(
           request=request,
           template_name='blog/recetas.html',
           context=contexto,
       )
       return http_response
   
def buscar_articulo(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       articulo = Articulos.objects.filter(
           Q(autor__icontains= busqueda) | Q(cafeteria_reseniada__nombre__icontains= busqueda) | Q(titulo__icontains= busqueda)    
       )
       contexto = {
           "articulos": articulo,
       }
       http_response = render(
           request=request,
           template_name='blog/articulos.html',
           context=contexto,
       )
       return http_response


#listView
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

#create view
def crear_cafeteria(request):
   if request.method == "POST":
       formulario = CafeteriaFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           direccion = data["direccion"]
           cafeteria = Cafeterias(nombre=nombre, direccion=direccion)  # lo crean solo en RAM
           cafeteria.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista 
           url_exitosa = reverse('lista_cafeterias')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = CafeteriaFormulario()

   http_response = render(
       request=request,
       template_name='blog/formulario_cafeterias.html',
       context={'formulario': formulario},
   )
   return http_response

def crear_articulo(request):
   if request.method == "POST":
       formulario = ArticulosFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           autor = data["autor"]
           cafeteria_reseniada = data["cafeteria_reseniada"]
           titulo = data["titulo"]
           texto = data["texto"]
           puntaje = data["puntaje"]

           articulo = Articulos(autor=autor, cafeteria_reseniada=cafeteria_reseniada, titulo=titulo, texto=texto, puntaje=puntaje)  # lo crean solo en RAM
           articulo.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista 
           url_exitosa = reverse('lista_articulos')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = ArticulosFormulario()

   http_response = render(
       request=request,
       template_name='blog/formulario_articulos.html',
       context={'formulario': formulario},
   )
   return http_response

def crear_receta(request):
   if request.method == "POST":
       formulario = RecetasFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           receta = data["receta"]
           receta = Recetas(nombre=nombre, receta=receta)  # lo crean solo en RAM
           receta.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista 
           url_exitosa = reverse('lista_recetas')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = RecetasFormulario()

   http_response = render(
       request=request,
       template_name='blog/formulario_recetas.html',
       context={'formulario': formulario},
   )
   return http_response




