from django.urls import path
from AppCoder import views
from AppCoder.views import crea_docente, crea_directivo, crea_alumno, crea_curso, cursos, docentes, alumnos, directivos, inicio, busquedaCurso, buscar


urlpatterns = [
    path("", inicio, name="inicio"),
    path("creaCurso", crea_curso),
    path("creaAlumno", crea_alumno),
    path("creaDirectivo", crea_directivo),
    path("creaDocente", crea_docente),
    path("alumnos", alumnos, name="alumnos"),
    path("cursos", cursos, name="cursos"),
    path("docentes", docentes, name="docentes"),
    path('directivos', directivos, name="directivos"),
    path("busquedaCurso", busquedaCurso, name="busquedaCurso"),
    path("buscar", buscar, name="buscar")

]