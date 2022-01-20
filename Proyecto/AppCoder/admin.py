from django.contrib import admin

from AppCoder.models import Alumno, Curso, Docentes, Directivos

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Docentes)
admin.site.register(Curso)
admin.site.register(Directivos)
