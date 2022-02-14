from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from AppCoder.models import Avatar, Curso, Alumno, Docente, Directivo
from AppCoder.forms import AvatarForm, FormDocente, FormDirectivo, FormCurso, FormAlumno, UserEditForm


def inicio(request):

    return render(request, "AppCoder/Inicio.html", )

def about(request):
    return render(request, "AppCoder/About.html")

#########################################################################################

def alumnos(request):
    lista_alumnos = Alumno.objects.all()
    return render(request, "AppCoder/Alumnos.html", {"lista": lista_alumnos})

class AlumnoList(LoginRequiredMixin ,ListView):
    model= Alumno
    template_name= "AppCoder/AlumnoList.html"

class AlumnoDetail(DetailView):
    model= Alumno
    template_name= "AppCoder/AlumnoDetail.html"

class AlumnoUpdate(UpdateView):
    model= Alumno
    success_url= "/AppCoder/listaAlumno"
    fields= ["nombre", "apellido", "dni", "año_nacimiento", "domicilio_calle",
    'domicilio_calleNumero', 'domicilio_cp', 'domicilio_localidad', 'provincia',
    'telefono_contacto']
    template_name= "AppCoder/AlumnoUpdate.html"

class AlumnoDelete(DeleteView):
    model= Alumno
    success_url= "/AppCoder/listaAlumno"
    template_name= "AppCoder/AlumnoConfirmDelete.html"

class AlumnoCreate(CreateView):
    model= Alumno
    success_url= "/AppCoder/listaAlumno"
    fields= ["nombre", "apellido", "dni", "año_nacimiento", "domicilio_calle",
    'domicilio_calleNumero', 'domicilio_cp', 'domicilio_localidad', 'provincia',
    'telefono_contacto']
    template_name= "AppCoder/AlumnoNew.html"

 
#########################################################################################
class DocenteList(LoginRequiredMixin ,ListView):
    model= Docente
    template_name= "AppCoder/DocenteList.html"

class DocenteDetail(DetailView):
    model= Docente
    template_name= "AppCoder/DocenteDetail.html"

class DocenteUpdate(UpdateView):
    model= Docente
    success_url= "/AppCoder/listaDocente"
    fields= ["nombre", "apellido", "dni", "telefono_contacto", "email"]
    template_name= "AppCoder/DocenteUpdate.html"

class DocenteDelete(DeleteView):
    model= Docente
    success_url= "/AppCoder/listaDocente"
    template_name= "AppCoder/DocenteConfirmDelete.html"

class DocenteCreate(CreateView):
    model= Docente
    success_url= "/AppCoder/listaDocente"
    fields= ["nombre", "apellido", "dni", "telefono_contacto", "email"]
    template_name= "AppCoder/DocenteNew.html"


#########################################################################################

class CursoList(LoginRequiredMixin ,ListView):
    model= Curso
    template_name= "AppCoder/CursoList.html"

class CursoDetail(DetailView):
    model= Curso
    template_name= "AppCoder/CursoDetail.html"

class CursoUpdate(UpdateView):
    model= Curso
    success_url= "/AppCoder/listaCurso"
    fields= ["grado", "division", "turno", "año"]
    template_name= "AppCoder/CursoUpdate.html"

class CursoDelete(DeleteView):
    model= Curso
    success_url= "/AppCoder/listaCurso"
    template_name= "AppCoder/CursoConfirmDelete.html"

class CursoCreate(CreateView):
    model= Curso
    success_url= "/AppCoder/listaCurso"
    fields= ["grado", "division", "turno", "año"]
    template_name= "AppCoder/CursoNew.html"


#########################################################################################    
class DirectivoList(LoginRequiredMixin ,ListView):
    model= Directivo
    template_name= "AppCoder/DirectivoList.html"

class DirectivoDetail(DetailView):
    model= Directivo
    template_name= "AppCoder/DirectivoDetail.html"

class DirectivoUpdate(UpdateView):
    model= Directivo
    success_url= "/AppCoder/listaDirectivo"
    fields= ["nombre", "apellido", "dni", "telefono_contacto"]
    template_name= "AppCoder/DirectivoUpdate.html"

class DirectivoDelete(DeleteView):
    model= Directivo
    success_url= "/AppCoder/listaDirectivo"
    template_name= "AppCoder/DirectivoConfirmDelete.html"

class DirectivoCreate(CreateView):
    model= Directivo
    success_url= "/AppCoder/listaDirectivo"
    fields= ["nombre", "apellido", "dni", "telefono_contacto"]
    template_name= "AppCoder/DirectivoNew.html"


#########################################################################################


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
            
            docente.nombre = data["nombre"]
            docente.apellido = data["apellido"]
            docente.dni = data["dni"]
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



##########################################################################################

def Login(request):
    if (request.method == "POST"):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)

                avatar = Avatar.objects.filter(user=request.user.id)

                return render(request, "AppCoder/Inicio.html", {'url': avatar[0].imagen.url} )

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

def editarPerfil(request):
    
    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if (mi_formulario.is_valid()):

            data = mi_formulario.cleaned_data
            
            usuario.first_name = data['first_name']            
            usuario.last_name = data['last_name']
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()
        
            return render(request, "AppCoder/Inicio.html")
            
    else:
        mi_formulario = UserEditForm(initial={"email": usuario.email})

        return render(request, "AppCoder/EditarPerfil.html", {"form": mi_formulario, "usuario": usuario} )

@login_required
def agregarAvatar(request):

    if request.method == "POST":

        mi_formulario = AvatarForm(request.POST, request.FILES)

        if (mi_formulario.is_valid()):

            user = User.objects.get(username=request.user)

            avatar = Avatar(user=user, imagen=mi_formulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, "AppCoder/Inicio.html")
            
    else:

        mi_formulario = AvatarForm()

        return render(request, "AppCoder/AgregarAvatar.html", {"form": mi_formulario} )



