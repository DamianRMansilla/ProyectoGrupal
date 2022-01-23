from django.db import models
class Alumno(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    dni = models.IntegerField(null=True)
    año_nacimiento = models.DateField("fecha", auto_now=False, auto_now_add=False)
    telefono_contacto = models.IntegerField(null=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} '

class Docente(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    telefono_contacto = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}-{self.apellido} '
class Curso(models.Model):
    grado = models.IntegerField()
    division = models.CharField("division", max_length=1)

    def __str__(self):
        return f'{self.grado}-{self.division}'

class Directivo(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre}-{self.apellido} '
