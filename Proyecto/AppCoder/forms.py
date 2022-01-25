from django import forms
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
    
