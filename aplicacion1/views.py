from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from aplicacion1.forms import AlumnoForm, LoginForm, CorreoForm, FotoForm
from aplicacion1.models import Alumno, Correo, Foto

import xlwt

# Create your views here.

def inicio (request):
    return render (request, 'aplicacion1/index.html')

#def page_not_found_view(request, exception): #mensaje de error
    #return render(request, '404.html', status=404)

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
            html_content=render_to_string('aplicacion1/email_template.html')
            to_email = str(form['email'].value())
            msg = EmailMultiAlternatives('Confirmacion registro Ex-Alunni SIV',html_content, 'exalunnisiv2022@gmail.com',[to_email,])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

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

def correo_todos(request):
    form = CorreoForm()
    if request.method == "POST":
        form=CorreoForm(data=request.POST)
        if form.is_valid():
            correo=Correo()
            correo.asunto=form.cleaned_data['asunto']
            correo.mensaje=form.cleaned_data['mensaje']
            correo.save()
            subject=request.POST.get('asunto')
            #html_content=render_to_string('aplicacion1/correo_todos.html')
            email_to=[]
            for alumno in Alumno.objects.all():
                email_to.append(alumno.email)
            #print (email_to)
            #to_email = str(form['email'].value())
            msg = EmailMultiAlternatives(subject,"html_content", 'exalunnisiv2022@gmail.com',email_to)
            #msg.attach_alternative(html_content, "text/html")
            msg.send()

        return redirect('/correo_todos')
    else:
        form = CorreoForm()
        return render (request, 'aplicacion1/correo_todos.html',{"form":form})  

def fotos_galeria(request):
    fotos=Foto.objects.all()
    return render (request,'aplicacion1/fotos_galeria.html',{"fotos":fotos})

def fotos_ingreso(request):  # ingreso de nuevos productos
    form = FotoForm()
    if request.method == "POST":
        form=FotoForm(data=request.POST, files=request.FILES)
        foto=form.save (commit=False)
        foto.save()
        return redirect('fotos_galeria')

    else:
        return render (request, 'aplicacion1/fotos_ingreso.html',{"form":form})

