
from django import forms
from  blog.models import Cafeterias,Articulos,Recetas

from ckeditor.widgets import CKEditorWidget

class RecetasFormulario(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = ('nombre', 'receta')
        widgets = {
            'texto': CKEditorWidget(),
        }

class CafeteriaFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    direccion = forms.CharField(required=True, max_length=1024)


class ArticulosFormulario(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ('cafeteria_reseniada', 'titulo', 'texto', 'puntaje')
        widgets = {
            'texto': CKEditorWidget(),
        }
''''
class ArticulosFormulario(forms.Form):
    autor = forms.CharField(required=True,max_length=64)
    cafeteria_reseniada= forms.ModelChoiceField(required=True,queryset=Cafeterias.objects.all())
    
    titulo = forms.CharField(required=True,max_length=64)
    texto = forms.CharField(required=True,widget=forms.Textarea)
    puntaje = forms.IntegerField(required=True, min_value=1, max_value=5)
'''
'''
class RecetasFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    receta = forms.CharField(required=True,widget=forms.Textarea)
'''