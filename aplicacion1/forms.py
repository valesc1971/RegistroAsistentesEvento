from django import forms
from django.db.models import fields
from .models import Alumno, Correo

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'email', 'generacion')

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)


class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ('asunto', 'mensaje')



