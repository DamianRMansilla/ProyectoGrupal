from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    path("pages/", views.paginas, name="paginas"),

    path("buscarAlumno/", views.buscar_alumno, name="buscarAlumno"),
    path("buscarCurso/", views.buscar_curso, name="buscarCurso"),
    path("buscarDirectivo/", views.buscar_directivo, name="buscarDirectivo"),
    path("buscarDocente/", views.buscar_docente, name="buscarDocente"),

    path("busquedaAlumno/", views.busqueda_alumno, name="busquedaAlumno"),
    path("busquedaCurso/", views.busqueda_curso, name="busquedaCurso"),
    path("busquedaDirectivo/", views.busqueda_directivo, name="busquedaDirectivo"),
    path("busquedaDocente/", views.busqueda_docente, name="busquedaDocente"),

    path("eliminarAlumno/<id_alumno>/", views.elimina_alumno, name="eliminaAlumno"),
    path("alumnos/", views.alumnos, name="alumnos"),
    # path("creaAlumno/", views.crea_alumno),

    path("listaAlumno/", views.AlumnoList.as_view(), name="VistaAlumno"),
    path("detalleAlumno/<pk>/", views.AlumnoDetail.as_view(), name="DetailAlumno"),
    path("actualizaAlumno/<pk>/", views.AlumnoUpdate.as_view(), name="EditAlumno"),
    path("eliminaAlumno/<pk>/", views.AlumnoDelete.as_view(), name="DeleteAlumno"),
    path("crearAlumno/", views.AlumnoCreate.as_view(), name="NewAlumno"),

    path("listaDocente/", views.DocenteList.as_view(), name="VistaDocente"),
    path("detalleDocente/<pk>/", views.DocenteDetail.as_view(), name="DetailDocente"),
    path("actualizaDocente/<pk>/", views.DocenteUpdate.as_view(), name="EditDocente"),
    path("eliminaDocente/<pk>/", views.DocenteDelete.as_view(), name="DeleteDocente"),
    path("crearDocente/", views.DocenteCreate.as_view(), name="NewDocente"),

    path("listaCurso/", views.CursoList.as_view(), name="VistaCurso"),
    path("detalleCurso/<pk>/", views.CursoDetail.as_view(), name="DetailCurso"),
    path("actualizaCurso/<pk>/", views.CursoUpdate.as_view(), name="EditCurso"),
    path("eliminaCurso/<pk>/", views.CursoDelete.as_view(), name="DeleteCurso"),
    path("crearCurso/", views.CursoCreate.as_view(), name="NewCurso"),

    path("listaDirectivo/", views.DirectivoList.as_view(), name="VistaDirectivo"),
    path("detalleDirectivo/<pk>/", views.DirectivoDetail.as_view(), name="DetailDirectivo"),
    path("actualizaDirectivo/<pk>/", views.DirectivoUpdate.as_view(), name="EditDirectivo"),
    path("eliminaDirectivo/<pk>/", views.DirectivoDelete.as_view(), name="DeleteDirectivo"),
    path("crearDirectivo/", views.DirectivoCreate.as_view(), name="NewDirectivo"),

    path("login/", views.Login, name="login"),
    path("register/", views.Register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/Logout.html"), name="logout"),

    path("editarPerfil/", views.editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", views.agregarAvatar, name="agregarAvatar"),  

]   