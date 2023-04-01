from django.urls import path
from AppCoder.views import cursos, estudiantes, profesores, crear_curso, busqueda_curso, crear_curso1, eliminar_curso, editar_curso

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('cursos/crear', crear_curso, name="AppCoderCrearCurso"),
    path('cursos/eliminar/<camada>', eliminar_curso, name="AppCoderEliminarCurso"),
    path('cursos/editar/<camada>', editar_curso, name="AppCoderEditarCurso"),
    path('buscar_curso', busqueda_curso, name="AppCoderBuscarCursos"),
    path('curso/<nombre>/<camada>', crear_curso1, name="AppCoderCurs"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderCursosProfesores"),
]