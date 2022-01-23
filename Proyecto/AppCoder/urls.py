from django.urls import path
from AppCoder import views
from AppCoder.views import busqueda_curso, buscar_curso, buscar_alumno, busqueda_alumno, crea_docente, crea_directivo, crea_alumno, crea_curso, cursos, docentes, alumnos, directivos, inicio


urlpatterns = [
    path("", inicio, name="inicio"),
    path("creaCurso/", crea_curso),
    path("creaAlumno/", crea_alumno),
    path("creaDirectivo/", crea_directivo),
    path("creaDocente/", crea_docente),
    path("alumnos/", alumnos, name="alumnos"),
    path("cursos/", cursos, name="cursos"),
    path("docentes/", docentes, name="docentes"),
    path('directivos/', directivos, name="directivos"),
    path("busquedaAlumno/", busqueda_alumno, name="busquedaAlumno"),
    path("buscarAlumno/", buscar_alumno, name="buscarAlumno"),
    path("busquedaCurso/", busqueda_curso, name="busquedaCurso"),
    path("buscarCurso/", buscar_curso, name="buscarCurso")

]