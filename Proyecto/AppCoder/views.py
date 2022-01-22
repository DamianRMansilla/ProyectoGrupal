from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso, Alumno, Docente, Directivo

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
        curso = Curso(req.POST["grado"], req.POST["division"])

        curso.save()

        return render(req, "inicio.html")

    return render(req, "AppCoder/CursoNuevo.html")



    
    

# def crea_curso(self):
#     curso = Curso(grado = "5", division = "A")
#     curso.save()

#     return HttpResponse(f'Se creo el curso {curso.grado}{curso.division}')
