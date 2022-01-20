from django.db import models
class Alumno(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    año_nacimiento = models.DateField("fecha", auto_now=False, auto_now_add=False)
    telefono_contacto = models.IntegerField(null=True)

class Docentes(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    telefono_contacto = models.IntegerField()

class Curso(models.Model):
    grado = models.IntegerField()
    division = models.CharField("division", max_length=1)

class Directivos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)

