
# Cómo configurar una aplicación de python en IIS
En algunas ocasiones vamos a requerir configurar una aplicación web en el IIS de un servidor windows, por uno u otra razón. 
Aquí voy a dejar los pasos que a la fecha de publicar este tutorial me han funcionado, espero les sirva y si encuentras una mejor manera, por favor
compartela.

## Antes de iniciar
Instalar el paquete para IIS que nos permitirá interpretar los archivos de python usando
WSGI y FastCGI

    pip install wfastcgi

Habilitemos el wfastcgi ejecutando el archivo `wfastcgi-enable.exe` ubicado en el directorio C:\python\Scripts

Copiamos el archivo `wfastcgi.py` ubicado en el directorio *C:\python\Lib\site-packages* a la ruta donde están ubicadas las aplicaciones del IIS, en este caso sería *C:\inetpub\www\mysite*

La documentación de este paquete se puede encontrar [aquí](https://pypi.org/project/wfastcgi/)

### Código de la aplicación de ejemplo

#### main.py
El código que voy a usar para la app de ejemplo es el siguiente:

    from flask import Flask
    app = Flask(__name__)
    
    @app.route("/")
    def hello():
	    return "Python saluda desde el IIS"
	
	if __name__ == "__main__":
		app.run()

#### web.config
También tendremos el siguiente código de configuración para el IIS:

    <configuration>  
	    <appSettings>  
		    <!-- Required settings -->  
		    <add key="WSGI_HANDLER" value="main.app" />  
		    <add key="PYTHONPATH" value="C:\inetpub\www\mysite\" /> 
		    <add key="WSGI_LOG" value="C:\inetpub\www\mysite\logs\wsgi.log" />
	    </appSettings>
    </configuration>

## Configuremos el IIS

 1. **Configurar el Handler Mappings o Asignaciones de controlador**
	 - En la raíz del IIS abrimos la opción *Hander Mappings*
	 - Seleccionamos la opción *Add module mapping o Agregar asignación de módulo*
	 - Configuramos los siguientes valores:
		 + Request path: *
		 + Module: FastCgiModule
		 + Executable: C:\python\python.exe|C:\inetpub\www\mysite\wfastcgi.py
		 + Name: Python FastCGI
		 + Seleccionamos la opción *Request Restrictions o Restricciones de solicitudes* y desmarcamos la opción *Invoke handler only... o Invocar controlador solo...*
		 + Aplicamos los cambios
 2. **Configuramos el pool de aplicaciones que atenderá las peticiones de nuestra app**
	 - Vamos al *Application pools* del IIS
	 - Seleccionamos el pool de aplicaciones asignado a nuestra aplicación
	 - Indicamos que deseamos modificar la ***configuración avanzada*** del pool
	 - En la propiedad versión de .Net framework seleccionamos la opción *No managed code o Sin código administrado*
	 - En la propiedad *Identity o Identidad* seleccionamos la opción ***LocalSystem***
	 - Aplicamos los cambios

Con esto debería funcionar la aplicación correctamente, sino es asi, vaya a la raíz del IIS e ingrese a la opción *FastCGI Settings o Configuración de FastCGI*. Si no existe un campo en el que el full path sea igual a *C:\python\python.exe* donde su argumento sea *C:\inetpub\www\mysite\wfastcgi.py*, registrelo.

Terminado esto, probamos ingresando la url de la aplicación en un explorador web y se debería ver el mensaje `Python saluda desde el IIS`.
