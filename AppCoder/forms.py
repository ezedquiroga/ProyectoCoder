from django import forms
from AppCoder.models import Estudiantes, Profesor

class CursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    camada = forms.IntegerField(min_value=1000)

class EstudiantesForm(forms.ModelForm):

    class Meta:
        model = Estudiantes
        fields = "__all__"

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = "__all__"

class BusquedaCursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)