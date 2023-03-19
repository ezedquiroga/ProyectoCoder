from django.urls import path
from AppCoder.views import cursos, estudiantes, profesores, crear_curso

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCurs"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderCursosProfesores"),
]