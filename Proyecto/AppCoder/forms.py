from django import forms
class formCurso(forms.Form):
    grado = forms.IntegerField()
    division = forms.CharField()

class formAlumno(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    año_nacimiento = forms.DateField()
    telefono_contacto = forms.IntegerField()

class formDocente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    telefono_contacto = forms.IntegerField()   
     
class formDirectivo(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    
