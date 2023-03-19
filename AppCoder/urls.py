from django.urls import path
from AppCoder.views import cursos, estudiantes, profesores, crear_curso, busqueda_curso

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('buscar_curso', busqueda_curso, name="AppCoderBuscarCursos"),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCurs"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderCursosProfesores"),
]