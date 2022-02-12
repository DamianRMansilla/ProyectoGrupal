from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormCurso(forms.Form):
    grado = forms.IntegerField()
    division = forms.CharField()

class FormAlumno(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    año_nacimiento = forms.DateField()
    telefono_contacto = forms.IntegerField()

class FormDocente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    telefono_contacto = forms.IntegerField()   
     
class FormDirectivo(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    
class FormDirectivo(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()





class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2' ]