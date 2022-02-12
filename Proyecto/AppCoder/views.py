from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from AppCoder.models import Curso, Alumno, Docente, Directivo
from AppCoder.forms import FormDocente, FormDirectivo, FormCurso, FormAlumno

def inicio(request):
    return render(request, "AppCoder/Inicio.html")

def about(request):
    return render(request, "AppCoder/About.html")

def alumnos(request):
    lista_alumnos = Alumno.objects.all()
    return render(request, "AppCoder/Alumnos.html", {"lista": lista_alumnos})
 
def docentes(request):
    lista_docentes = Docente.objects.all()
    return render(request, "AppCoder/Docente.html", {"lista": lista_docentes})

def cursos(request):
    lista_cursos = Curso.objects.all()
    return render(request, "AppCoder/Cursos.html", {"lista": lista_cursos})

@login_required
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

def elimina_curso(request, id_curso):
    curso = Curso.objects.get(id=id_curso)

    curso.delete()

    lista_cursos = Curso.objects.all()

    return render(request, "AppCoder/Cursos.html", {"lista": lista_cursos})

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

def elimina_alumno(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)

    alumno.delete()

    lista_alumnos = Alumno.objects.all()

    return render(request, "AppCoder/Alumnos.html", {"lista": lista_alumnos})

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

def elimina_directivo(request, id_directivo):
    directivo = Directivo.objects.get(id=id_directivo)

    directivo.delete()

    lista_directivos = Directivo.objects.all()

    return render(request, "AppCoder/Directivos.html", {"lista": lista_directivos})

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

def elimina_docente(request, id_docente):
    docente = Docente.objects.get(id=id_docente)

    docente.delete()

    lista_docentes = Docente.objects.all()

    return render(request, "AppCoder/Docente.html", {"lista": lista_docentes})

def editar_docente(request, docente_nombre):
    docente = Docente.objects.get(nombre = docente_nombre)

    if request.method == "POST":
        mi_formulario = FormDocente(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            
            docente.nombre = data["nombre"], 
            docente.apellido = data["apellido"], 
            docente.dni = data["dni"],
            docente.telefono_contacto = data["telefono_contacto"]
                               
            docente.save()
            return render(request, "AppCoder/Inicio.html")
            
    else:
        mi_formulario = FormDocente(initial={"nombre": docente.nombre, 
                                            "apellido": docente.apellido, 
                                            "dni": docente.dni, 
                                            "telefono_contacto": docente.telefono_contacto})

    return render(request, "AppCoder/EditarDocente.html", {"form": mi_formulario, "docente_nombre": docente_nombre})

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


#####################################################################################

class CursoList(LoginRequiredMixin ,ListView):
    model= Curso
    template_name= "AppCoder/Curso_list.html"

class CursoDetail(DetailView):
    model= Curso
    template_name= "AppCoder/Curso_detalle.html"

class CursoUpdate(UpdateView):
    model= Curso
    success_url= "/AppCoder/listaCursos"
    fields= ["grado", "division"]
    template_name= "AppCoder/Curso_form.html"

class CursoDelete(DeleteView):
    model= Curso
    success_url= "/AppCoder/listaCursos"
    template_name= "AppCoder/Curso_confirm_delete.html"

class CursoCreate(CreateView):
    model= Curso
    success_url= "/AppCoder/listaCursos"
    fields= ["grado", "division"]
    template_name= "AppCoder/Cursos1.html"


##########################################################################################

def Login(request):
    if (request.method == "POST"):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/Inicio.html", {"mensaje": f'Bienvenido {user.get_username()}'})

            else:
                return render(request, "AppCoder/Inicio.html", {"mensaje": "Error, datos incorrectos"})

        else:
            return render(request, "AppCoder/Inicio.html", {"mensaje": "Error, formulario errorneo"})

    else:
        form  = AuthenticationForm()

        return render(request, "AppCoder/Login.html", {"form": form})

def Register(request):
    if (request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/Inicio.html", {"mensaje": "Usuario creado exitosamente"})

        else:
            return render(request, "AppCoder/Inicio.html", {"mensaje": "Informacion de registro incorrecta"})
        
    else:
        form = UserCreationForm()

        return render(request, "AppCoder/Registro.html", {"form": form})