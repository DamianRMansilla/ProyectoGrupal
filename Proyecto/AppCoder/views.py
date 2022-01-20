from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso, Alumno, Docentes, Directivos

def alumnos(request):
    listaDeAlumnos = Alumno.objects.all()
    return render(request, "Alumnos.html", {"lista": listaDeAlumnos})
 
def docentes(request):
    listaDeDocentes = Docentes.objects.all()
    return render(request, "Docentes.html", {"lista": listaDeDocentes})

def cursos(request):
    listaDeCursos = Curso.objects.all()
    return render(request, "Cursos.html", {"lista": listaDeCursos})

def directivos(request):
    listaDeDirectivos = Directivos.objects.all()
    return render(request, "Directivos.html", {"lista": listaDeDirectivos})


def crea_curso(req):

    if (req.method == "POST"):
        curso = Curso(req.POST["grado"], req.POST["division"])

        curso.save()

        return render(req, "inicio.html")

    return render(req, "CursoNuevo.html")



    
    

# def crea_curso(self):
#     curso = Curso(grado = "5", division = "A")
#     curso.save()

#     return HttpResponse(f'Se creo el curso {curso.grado}{curso.division}')
