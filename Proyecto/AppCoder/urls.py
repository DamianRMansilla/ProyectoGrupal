from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("alumnos/", views.alumnos, name="alumnos"),
    path("cursos/", views.cursos, name="cursos"),
    path("docentes/", views.docentes, name="docentes"),
    path('directivos/', views.directivos, name="directivos"),
    path('about/', views.about, name="about"),
    
    path("creaCurso/", views.crea_curso),
    path("creaAlumno/", views.crea_alumno),
    path("creaDirectivo/", views.crea_directivo),
    path("creaDocente/", views.crea_docente),

    path("buscarAlumno/", views.buscar_alumno, name="buscarAlumno"),
    path("buscarCurso/", views.buscar_curso, name="buscarCurso"),
    path("buscarDirectivo/", views.buscar_directivo, name="buscarDirectivo"),
    path("buscarDocente/", views.buscar_docente, name="buscarDocente"),

    path("busquedaAlumno/", views.busqueda_alumno, name="busquedaAlumno"),
    path("busquedaCurso/", views.busqueda_curso, name="busquedaCurso"),
    path("busquedaDirectivo/", views.busqueda_directivo, name="busquedaDirectivo"),
    path("busquedaDocente/", views.busqueda_docente, name="busquedaDocente"),

    path("eliminarDocente/<id_docente>/", views.elimina_docente, name="eliminaDocente"),
    path("eliminarAlumno/<id_alumno>/", views.elimina_alumno, name="eliminaAlumno"),
    path("eliminarDirectivo/<id_directivo>/", views.elimina_directivo, name="eliminaDirectivo"),
    path("eliminarCurso/<id_curso>/", views.elimina_curso, name="eliminaCurso"),

    path("editarDocente/<docente_nombre>/", views.editar_docente, name="editarDocente"),

    path("listaCursos/", views.CursoList.as_view(), name="VistaCursos"),
    path("detalleCursos/<pk>/", views.CursoDetail.as_view(), name="Detail"),
    path("actualizaCursos/<pk>/", views.CursoUpdate.as_view(), name="Edit"),
    path("eliminaCursos/<pk>/", views.CursoDelete.as_view(), name="Delete"),
    path("crearCursos/", views.CursoCreate.as_view(), name="New"),

    path("login/", views.Login, name="login"),
    path("register/", views.Register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/Logout.html"), name="logout"),

    path("editarPerfil/", views.editarPerfil, name="editarPerfil"),
    

]   