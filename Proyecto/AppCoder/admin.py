from django.contrib import admin

from AppCoder.models import Alumno, Curso, Docente, Directivo

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Directivo)
