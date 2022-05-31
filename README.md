# RegistroAsistentesEvento

Este proyecto consiste en el desarrollo de una aplicacion para registrar asistentes a un evento.

Esta aplicacion permite el registro de los asistentes en una base de datos y en envio de un email de notificacion; la visualizacion de los datos en una tabla 
y la descarga de estos a una planilla excel; el envio de un email masivo a todos los contactos registrados; y la posibilidad de subir fotografias del eventos y 
visualizarlas en una galeria.


## Tabla de Contenidos

* [Tecnologias Usadas](#Tecnologias)
* [Instalacion](#Instalacion)
* [Consideraciones](#Consideraciones)
* [Funcionalidad y Visualizacion](#Funcionalidad y Visualizacion)


<a name="Tecnologias"></a>
## Tecnologias

Este proyecto fue creado usando:
* HTML
* CSS
* Boostrap   (https://getbootstrap.com/)
* JavaScript (https://datatables.net/)
* JQuery    (https://jquery.com/)
* DataTable plugin (https://datatables.net/)
* Python (https://www.python.org/)
* Django (https://www.djangoproject.com/)
* PostgreSQL (https://www.postgresql.org/)
* SweetAlert plugin (https://sweetalert.js.org/)
* Cloudinary (https://cloudinary.com/)

El detalle de las librerias y versiones utilizadas se encuentra en el archivo requirements.txt

<a name="Instalacion"></a>
## Instalacion

**Clonar repositorio desde Github**

Para descargar este proyecto, se debe clonar desde este repositorio remoto a un repositorio local.

1. Abrir GitBash
2. Ubicarse en el directorio de la ubicacion donde se quiere clonar la aplicacion
3. Escribir   $git clone https://github.com/valesc1971/RegistroAsistentesEvento.gi
4. Hacer Enter para clonar el repositorio 

**Crear entorno virtual**

Se debe tambien correr dentro de un entorno virtual de Python (virtualenv) (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

1. Instalar pip
py -m pip install --upgrade pip
py -m pip --version

2. Instalar virtualenv
py -m pip install --user virtualenv

3. Crear el entorno virtual
py -m venv env

4. Activar el entorno virtual 
.\env\Scripts\activate

5. Salir del entorno virtual
deactivate

**Instalar librerias adicionales**
Las librerías instaladas se encuentran en el archivo requirements.txt. Para instalar, se debe hacer lo siguientes

$ pip install -r requirements.txt


<a name="Consideraciones"></a>
## Consideraciones

Para el desarrollo del codigo de frontend, se utilizo HTML como herramienta principal, utilizando CSS para el formato y las herramientas JavaScript, JQuery, 
Boostrap, DataTable, SweetAlert las que son llamadas usando CDNs.

Los archivos HTML se ubican dentro de un directorio dentro de la aplicacion llamado templates\aplicacion1

Se creo una plantilla de html (proyecto/templates/base_layout.html) que incluye la barra de navegacion, footer, y mensajes de alerta desplegados usando SweetAlert
Esta plantilla se llamada dentro de los archivos HTML principales y contiene tambien los archivos y CDNs para las herramientas de diseño. 

Los archivos de imagenes, el archivo style.css (CSS) y JS se encuentran dentro de un directorio static (aplicacion1\static)

El desarrollo del codigo de backend se hizo usando la framework django en conjunto con python.

<a name="Funcionalidad y Visualizacion"></a>
## Funcionalidad y Visualizacion

Se puede navegar a traves del sitio usando las opciones que entrega la barra de navegacion. Estas opciones son distintas dependiendo el tipo de permiso que tiene el usuario de la aplicacion (administrativo o no_administrativo). 
El tipo de permiso se establecio restringiendo la visibilidad de los links en la plantilla base (base_layout)

Inicio: Pantalla de inicio
Registro: Registro de asistentes
Ingreso-Admin: Ingreso de administrador de la aplicacion (pagina de login)
Tabla: Tabla con registros de usuarios
Salir_Admin: Desconeccion de administrador
Enviar Correo: enviar correo a todos los contactos registrados

![image](https://user-images.githubusercontent.com/99301347/170840683-5ffae1a2-0206-48d1-b768-ad4154bcc34e.png)


El usuario que ingresa a la aplicacion no_administrativo , tiene las acceso a las siguientes opciones:

Inicio
Registro
Galeria Fotos
Ingreso-Admin (esta opcion esta visible pero no permite ingresar a la administracion del sitio sin las claves de acceso.)

![image](https://user-images.githubusercontent.com/99301347/170840263-3c07abba-6ebf-486b-a090-4565fee2c48c.png)

El usuario administrativo (superuser) una vez que ingresa a traves de la opcion Ingreso-Admin, tiene acceso a

Inicio
Registro
Galeria Fotos
Ingreso-Admin
Tabla
Salir_Admin
Enviar Correo

![image](https://user-images.githubusercontent.com/99301347/170840437-163524d6-6c8c-4682-83b3-a12a55d58baf.png)

Cuando se ingresa un nuevo registro, se envia un mensaje informativo al correo registrado y se despliega tambien una alerta confirmando que el registro se ha creado. 
El correo se envia a partir de un archivo html (email_template.html) por lo que se puede modificar en caso de ser necesario.

![image](https://user-images.githubusercontent.com/99301347/170840495-b6449449-94e3-4fcf-b25e-2831a9f472f7.png)

El usuario puede ver las fotos en la opcion Galeria Fotos. En esta opcion tambien existe un boton que permite subir fotografias.

![image](https://user-images.githubusercontent.com/99301347/170840629-aded16af-8b52-4de2-b05a-d5e20301a7af.png)

![image](https://user-images.githubusercontent.com/99301347/170840638-59e4e2fe-0934-4fdb-b87c-b3bd58721483.png)

La opcion Ingresar permite al administrador de la aplicacion logearse

![image](https://user-images.githubusercontent.com/99301347/170840736-4a1fbaea-e29d-4535-be14-ce83e666661d.png)

El administrador de la aplicacion puede ver los datos registrado en la opcion Tabla.

En esta misma opcion, se pueden descargar los datos de la tabla en formato excel o editar o eliminar cada uno de los registros. 
Esta tabla es dinamica, por lo que permite tambien la busqueda, ordenamiento y filtro de registros.

![image](https://user-images.githubusercontent.com/99301347/170840477-d68b0791-a173-4e63-a17e-2d12eabf010d.png)
![image](https://user-images.githubusercontent.com/99301347/170840795-3e0e4b37-e45d-4111-bb17-bad99ac4351c.png)

En el caso de modificar un regitro, una vez modificado este se despliega un mensaje de confirmacion. 

En el caso de eliminacion del registro, se despliega un mensaje de confirmacion de la eliminacion

El envio de un correo masivo se hace desde la opcion Enviar Correo que esta visible solo si el administrador ha ingresado

![image](https://user-images.githubusercontent.com/99301347/170840530-c1ad3e2d-91f6-4ec9-83dd-a9d70a23223e.png)

Una vez que el administrador se desconecta con la opcions Salir-Admin, se despliega un mensaje de alerta

![image](https://user-images.githubusercontent.com/99301347/170840806-f564a695-8ee2-4711-84e8-45ad29e07367.png)












