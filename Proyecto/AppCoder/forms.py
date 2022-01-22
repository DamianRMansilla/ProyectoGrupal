from django import forms

class formCurso(forms.Form):
    grado = forms.IntegerField()
    division = forms.CharField()