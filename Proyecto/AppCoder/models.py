from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    turno_curso_choices = [('Mañana', 'Mañana'),('Tarde', 'Tarde')]


    grado = models.IntegerField()
    division = models.CharField("division", max_length=1)
    turno = models.CharField("turno", max_length=6, choices=turno_curso_choices, null=True)
    año = models.IntegerField(null=True)

    def __str__(self):
        return f'Curso: {self.grado} - Division: {self.division} - Turno: {self.turno} - Año {self.año} '

class Alumno(models.Model):
    provincias = [
        ('Buenos Aires','Buenos Aires'),
        ('Catamarca','Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes','Corrientes') ,
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán')
        ]

    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    dni = models.IntegerField(null=True)
    año_nacimiento = models.DateField("fecha", auto_now=False, auto_now_add=False)
    domicilio_calle = models.CharField("calle", max_length=200, null=True, blank=True)
    domicilio_calleNumero = models.IntegerField("calle n°", null=True, blank=True)
    domicilio_cp = models.IntegerField("código Postal", null=True, blank=True)
    domicilio_localidad = models.CharField("localidad", max_length=200, null=True, blank=True)
    provincia = models.CharField("provincia", max_length=50, choices=provincias, null=True, blank=True)
    telefono_contacto = models.IntegerField('teléfono de Contacto', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - DNI: {self.dni}'

class Docente(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    dni = models.IntegerField(null=True)
    telefono_contacto = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni}'


class Directivo(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni = models.IntegerField(null=True)
    telefono_contacto = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= 'avatares', null=True, blank=True)

    def __str__(self):
        return f'Imagen de {self.user.username} '
