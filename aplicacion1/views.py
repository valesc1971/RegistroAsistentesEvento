from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout

from aplicacion1.forms import AlumnoForm, LoginForm
from aplicacion1.models import Alumno

import xlwt

# Create your views here.

def inicio (request):
    return render (request, 'aplicacion1/index.html')

def login(request):   #ingreso de usuario admin
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request, user)
                messages.add_message(request, messages.INFO, f"Has ingresado como {usuario}." )
                return redirect ('inicio')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form= LoginForm()
    return render (request, 'aplicacion1/login.html', {"form":form})

def salir (request):  #salir usuario admin
    logout (request)
    messages.info(request, "Tu sesion ha terminado") 
    return redirect ("/login")

def registro_alumno(request):
    form = AlumnoForm()
    if request.method == "POST":
        form=AlumnoForm(data=request.POST)

        if form.is_valid():
            alumno=Alumno()
            alumno.nombre=form.cleaned_data['nombre']
            alumno.apellido_paterno=form.cleaned_data['apellido_paterno']
            alumno.apellido_materno=form.cleaned_data['apellido_materno']
            alumno.telefono=form.cleaned_data['telefono']
            alumno.email=form.cleaned_data['email']
            alumno.generacion=form.cleaned_data['generacion']
            alumno.save()
            messages.success(request, 'ingresado correctamente')
            

        return redirect('/registro_alumno')
    else:
        form = AlumnoForm()
        return render (request, 'aplicacion1/registro_alumno.html',{"form":form})

def listado (request):  #muestra mensajes recibidos
    listado=Alumno.objects.all()
    return render (request,'aplicacion1/listado.html',{"data":listado})

def editar_alumno(request, id):
    alumno=Alumno.objects.get(pk=id)
    form=AlumnoForm(instance=alumno)
    if request.method=="POST":
        form=AlumnoForm(data=request.POST, instance=alumno)
        form.save()
        messages.success(request, 'modificado correctamente')
        return redirect('/listado')
    else:
        return render (request, 'aplicacion1/editar_alumno.html',{"form":form})

def eliminar_alumno(request, id):
    alumno=Alumno.objects.get(pk=id)
    #if request.method=="POST":
    alumno.delete()
    messages.info(request, 'eliminado correctamente')
    return redirect('/listado')
    #return render (request, 'aplicacion1/eliminar_alumno.html')

def export_excel (request):
    response= HttpResponse(content_type='application/vnd.ms-excel')
    response['Content_Disposition'] = 'attachment; filename=Listado.xlsx'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Listado')
    
    row_num = 0 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Telefono', 'Email', 'Generacion']

    for col_num in range (len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows=Alumno.objects.all().values_list('nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'email', 'generacion')

    for row in rows:
        row_num+=1

        for col_num in range (len(row)):
            ws.write(row_num, col_num, row[col_num], font_style )
    
    wb.save(response)

    return response