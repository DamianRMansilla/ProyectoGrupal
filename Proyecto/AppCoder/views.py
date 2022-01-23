from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso, Alumno, Docente, Directivo
from AppCoder.forms import formDocente, formDirectivo, formCurso, formAlumno

def inicio(request):
    return render(request, "AppCoder/Inicio.html")

def alumnos(request):
    listaDeAlumnos = Alumno.objects.all()
    return render(request, "AppCoder/Alumnos.html", {"lista": listaDeAlumnos})
 
def docentes(request):
    listaDeDocentes = Docente.objects.all()
    return render(request, "AppCoder/Docente.html", {"lista": listaDeDocentes})

def cursos(request):
    listaDeCursos = Curso.objects.all()
    return render(request, "AppCoder/Cursos.html", {"lista": listaDeCursos})

def directivos(request):
    listaDeDirectivos = Directivo.objects.all()
    return render(request, "AppCoder/Directivos.html", {"lista": listaDeDirectivos})

def crea_curso(req):

    if (req.method == "POST"):

        mi_formulario = formCurso(req.POST)

        if (mi_formulario.is_valid()):

            curso = Curso(grado = req.POST["grado"], division = req.POST["division"])
            #return render(req, "AppCoder/CursoNuevo.html")

            curso.save()

            return render(req, "inicio.html")

    else:

        mi_formulario = formCurso()

    return render(req, "CursoNuevo.html", {"form": mi_formulario})

def crea_alumno(request):

    if (request.method == "POST"):
        mi_formulario = formAlumno(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            alumno = Alumno(nombre = data["nombre"], 
                            apellido = data["apellido"],
                            año_nacimiento = data["año_nacimiento"],
                            telefono_contacto = data["telefono_contacto"],
                            )
            alumno.save()
            return render(request, "AppCoder/Inicio.html")

    else:
        mi_formulario = formAlumno()

    return render(request, "AppCoder/AlumnoNuevo.html", {"form": mi_formulario})

def crea_directivo(request):

    if (request.method == "POST"):
        mi_formulario = formDirectivo(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            directivo  = Directivo(nombre = data["nombre"], 
                            apellido = data["apellido"],
                            )
            directivo.save()
            return render(request, "AppCoder/Inicio.html")
            
    else:
        mi_formulario = formDirectivo()

    return render(request, "AppCoder/DirectivoNuevo.html", {"form": mi_formulario})

def crea_docente(request):

    if (request.method == "POST"):
        mi_formulario = formDocente(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            docente  = Docente(nombre = data["nombre"], 
                               apellido = data["apellido"],
                               telefono_contacto = data["telefono_contacto"]
                               )
            docente.save()
            return render(request, "AppCoder/Inicio.html")
            
    else:
        mi_formulario = formDocente()

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

            return render(req, "ResultadoBusquedaCurso.html", {"grados": grados, "division": division})
        
            #return HttpResponse(f'Estamos buscnado los cursos de {req.GET["curso"]}°')

        else:
            respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
