from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
# Create your views here.
def guardar_curso(request):
    curso = Curso(nombre="Python", camada=23800)
    curso.save()
    return HttpResponse("usuario creado exitosamente")
