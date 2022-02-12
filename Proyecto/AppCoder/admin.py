from django.contrib import admin

from AppCoder.models import Alumno, Avatar, Curso, Docente, Directivo

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Directivo)
admin.site.register(Avatar)