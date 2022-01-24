from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("creaCurso/", views.crea_curso),
    path("creaAlumno/", views.crea_alumno),
    path("creaDirectivo/", views.crea_directivo),
    path("creaDocente/", views.crea_docente),
    path("alumnos/", views.alumnos, name="alumnos"),
    path("cursos/", views.cursos, name="cursos"),
    path("docentes/", views.docentes, name="docentes"),
    path('directivos/', views.directivos, name="directivos"),
    path("busquedaAlumno/", views.busqueda_alumno, name="busquedaAlumno"),
    path("buscarAlumno/", views.buscar_alumno, name="buscarAlumno"),
    path("busquedaCurso/", views.busqueda_curso, name="busquedaCurso"),
    path("buscarCurso/", views.buscar_curso, name="buscarCurso"),
    path("busquedaDirectivo/", views.busqueda_directivo, name="busquedaDirectivo"),
    path("buscarDirectivo/", views.buscar_directivo, name="buscarDirectivo"),
    path("busquedaDocente/", views.busqueda_docente, name="busquedaDocente"),
    path("buscarDocente/", views.buscar_docente, name="buscarDocente")


]