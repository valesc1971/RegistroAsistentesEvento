from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro_alumno/', views.registro_alumno, name='registro_alumno'),
    path('listado/', views.listado, name='listado'),
    path('editar_alumno/<int:id>', views.editar_alumno, name='editar_alumno'),
    path('eliminar_alumno/<int:id>', views.eliminar_alumno, name='eliminar_alumno'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('login/', views.login, name='login'),
    path('salir/', views.salir, name='salir'),
    path('correo_todos/', views.correo_todos, name='correo_todos'),
    path('fotos_ingreso/', views.fotos_ingreso, name='fotos_ingreso'),
    path('fotos_galeria/', views.fotos_galeria, name='fotos_galeria'),


]