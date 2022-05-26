from django.contrib import admin
from .models import Alumno, Correo, Foto

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Correo)
admin.site.register(Foto)
