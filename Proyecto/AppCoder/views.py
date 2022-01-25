from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso, Alumno, Docente, Directivo
from AppCoder.forms import FormDocente, FormDirectivo, FormCurso, FormAlumno

def inicio(request):
    return render(request, "AppCoder/Inicio.html")

def alumnos(request):
    lista_alumnos = Alumno.objects.all()
    return render(request, "AppCoder/Alumnos.html", {"lista": lista_alumnos})
 
def docentes(request):
    lista_docentes = Docente.objects.all()
    return render(request, "AppCoder/Docente.html", {"lista": lista_docentes})

def cursos(request):
    lista_cursos = Curso.objects.all()
    return render(request, "AppCoder/Cursos.html", {"lista": lista_cursos})

def directivos(request):
    lista_directivos = Directivo.objects.all()
    return render(request, "AppCoder/Directivos.html", {"lista": lista_directivos})

def crea_curso(request):

    if (request.method == "POST"):

        mi_formulario = FormCurso(request.POST)

        if (mi_formulario.is_valid()):

            curso = Curso(grado = request.POST["grado"], division = request.POST["division"])
            #return render(req, "AppCoder/CursoNuevo.html")

            curso.save()

            return render(request, "AppCoder/inicio.html")

    else:

        mi_formulario = FormCurso()

    return render(request, "AppCoder/CursoNuevo.html", {"form": mi_formulario})

def crea_alumno(request):

    if (request.method == "POST"):
        mi_formulario = FormAlumno(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            alumno = Alumno(nombre = data["nombre"], 
                            apellido = data["apellido"], 
                            dni = data["dni"],
                            año_nacimiento = data["año_nacimiento"],
                            telefono_contacto = data["telefono_contacto"],
                            )
            alumno.save()
            return render(request, "AppCoder/Inicio.html")

    else:
        mi_formulario = FormAlumno()

    return render(request, "AppCoder/AlumnoNuevo.html", {"form": mi_formulario})

def crea_directivo(request):

    if (request.method == "POST"):
        mi_formulario = FormDirectivo(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            directivo  = Directivo(nombre = data["nombre"], 
                            apellido = data["apellido"], 
                            dni = data["dni"]
                            )
            directivo.save()
            return render(request, "AppCoder/Inicio.html")
            
    else:
        mi_formulario = FormDirectivo()

    return render(request, "AppCoder/DirectivoNuevo.html", {"form": mi_formulario})

def crea_docente(request):

    if (request.method == "POST"):
        mi_formulario = FormDocente(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            docente  = Docente(nombre = data["nombre"], 
                               apellido = data["apellido"], 
                               dni = data["dni"],
                               telefono_contacto = data["telefono_contacto"]
                               )
            docente.save()
            return render(request, "AppCoder/Inicio.html")
            
    else:
        mi_formulario = FormDocente()

    return render(request, "AppCoder/DocenteNuevo.html", {"form": mi_formulario})

def busqueda_alumno(request):
    return render(request, "AppCoder/BusquedaAlumno.html")
    
def buscar_alumno(request):

    if request.GET["dni"]:

        dni = request.GET["dni"]
        alumnos = Alumno.objects.filter(dni__icontains=dni)

        return render(request, "AppCoder/ResultadoBusquedaAlumno.html", {"alumnos": alumnos, 'dni':dni})
    else:
        respuesta = "No enviaste datos"

    return render(request, 'AppCoder/Inicio.html', {'respuesta': respuesta})

def busqueda_curso(req):
    return render(req, "AppCoder/BusquedaCurso.html")
    
def buscar_curso(req):

    #if(req.method == "GET"):
        if(req.GET["division"]):
            division = req.GET["division"]
            grados = Curso.objects.filter(division__icontains=division)

            return render(req, "AppCoder/ResultadoBusquedaCurso.html", {"grados": grados, "division": division})
        
            #return HttpResponse(f'Estamos buscnado los cursos de {req.GET["curso"]}°')

        else:
            respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def busqueda_directivo(request):
    return render(request, "AppCoder/BusquedaDirectivo.html")

def buscar_directivo(request):

        if(request.GET["dni"]):
            dni = request.GET["dni"]
            directivos = Directivo.objects.filter(dni__icontains=dni)

            return render(request, "AppCoder/ResultadoBusquedaDirectivo.html", {"directivos": directivos, "dni": dni})

        else:
            respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def busqueda_docente(request):
    return render(request, "AppCoder/BusquedaDocente.html")

def buscar_docente(request):

        if(request.GET["dni"]):
            dni = request.GET["dni"]
            docentes = Docente.objects.filter(dni__icontains=dni)

            return render(request, "AppCoder/ResultadoBusquedaDocente.html", {"docentes": docentes, "dni": dni})

        else:
            respuesta = "No enviaste datos"
        return HttpResponse(respuesta)