from django.urls import path
from AppCoder import views
from AppCoder.views import crea_curso, cursos, docentes, alumnos, directivos, inicio

urlpatterns = [
    path("", inicio, name="inicio"),
    path("creaCurso/", crea_curso),
    path("alumnos/", alumnos, name="alumnos"),
    path("cursos/", cursos, name="cursos"),
    path("docentes/", docentes, name="docentes"),
    path('directivos/', directivos, name="directivos")

]