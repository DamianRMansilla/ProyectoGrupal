from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso, Alumno, Docente, Directivo
from AppCoder.forms import formCurso

def inicio(request):
    return render(request, "AppCoder/Inicio.html")


def alumnos(request):
    listaDeAlumnos = Alumno.objects.all()
    return render(request, "AppCoder/Alumnos.html", {"lista": listaDeAlumnos})
 
def docentes(request):
    listaDeDocentes = Docente.objects.all()
    return render(request, "AppCoder/Docentes.html", {"lista": listaDeDocentes})

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


def busquedaCurso(req):
    return render(req, "busquedaCurso.html")
    
def buscar(req):

    #if(req.method == "GET"):
        if(req.GET["division"]):
            division = req.GET["division"]
            grados = Curso.objects.filter(division__icontains=division)

            return render(req, "ResultadoBusqueda.html", {"grados": grados, "division": division})
        
            #return HttpResponse(f'Estamos buscnado los cursos de {req.GET["curso"]}°')

        else:
            respuesta = "No enviaste datos"
            return HttpResponse(respuesta)

# def crea_curso(self):
#     curso = Curso(grado = "5", division = "A")
#     curso.save()

#     return HttpResponse(f'Se creo el curso {curso.grado}{curso.division}')
