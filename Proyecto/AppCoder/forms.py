from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar


class FormCurso(forms.Form):
    grado = forms.IntegerField()
    division = forms.CharField()
    turno = forms.CharField()
    año = forms.IntegerField()
    imagen = forms.ImageField()

class FormAlumno(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    # año_nacimiento = forms.DateField()
    # domicilio_calle = forms.CharField()
    # domicilio_calleNumero = forms.IntegerField()
    # domicilio_cp = forms.IntegerField()
    # domicilio_localidad = forms.CharField()
    # provincia = forms.CharField()
    telefono_contacto = forms.IntegerField()
    imagen = forms.ImageField()


class FormDocente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    telefono_contacto = forms.IntegerField()
    imagen = forms.ImageField()
   
     
class FormDirectivo(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    telefono_contacto = forms.IntegerField()
    imagen = forms.ImageField()



class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2' ]



class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('user', 'imagen',)
