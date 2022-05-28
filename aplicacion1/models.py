from django.db import models

# Create your models here.

class Alumno(models.Model):
    rut=models.CharField(max_length=15, null=False)
    nombre=models.CharField(max_length=50, null=False)
    apellido_paterno=models.CharField(max_length=100, null=False)
    apellido_materno=models.CharField(max_length=100, null=False)
    telefono=models.CharField(max_length=100, null=False)
    email=models.EmailField()


    def __str__(self):
        return self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno    

class Correo(models.Model):
    asunto=models.CharField(max_length=100, null=False)
    mensaje=models.TextField(null=False)

    def __str__(self):
        return self.asunto

class Foto(models.Model):
    descripcion=models.CharField(max_length=500, null=False)
    imagen=models.ImageField(upload_to='fotos', blank=True, null=True, default='logoSIV.png')

    def __str__(self):
        return self.descripcion
