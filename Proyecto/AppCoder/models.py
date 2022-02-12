from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    grado = models.IntegerField()
    division = models.CharField("division", max_length=1)

    def __str__(self):
        return f'Curso: {self.grado} - Division: {self.division}'

class Alumno(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    dni = models.IntegerField(null=True)
    año_nacimiento = models.DateField("fecha", auto_now=False, auto_now_add=False)
    telefono_contacto = models.IntegerField(null=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni}'

class Docente(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    dni = models.IntegerField(null=True)
    telefono_contacto = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni}'


class Directivo(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni = models.IntegerField(null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= 'avatares', null=True, blank=True)

    def __str__(self):
        return f'Imagen de {self.user.username} '

