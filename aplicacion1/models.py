from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    apellido_paterno=models.CharField(max_length=100, null=False)
    apellido_materno=models.CharField(max_length=100, null=False)
    telefono=models.CharField(max_length=100, null=False)
    email=models.EmailField()
    generacion=models.CharField(max_length=15, null=False)

class Correo(models.Model):
    asunto=models.CharField(max_length=100, null=False)
    mensaje=models.TextField(null=False)



