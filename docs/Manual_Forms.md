



# Rocketbot Xperience
  
Module for Rocketbot Forms  
  
![banner](https://i.imgur.com/XC17kMx.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  



## Descripción de los comandos

### Login NOC
  
Login NOC
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de usuario|Nombre de usuario|User1|
|Contraseña|Contraseña del usuario|Password|
|Servidor|URL del servidor donde se conecta|https://roc.myrb.io/|
|-------------------------------------------------------------------------------------------------------|||
|API Key|API Key para conectarse al servidor|224f1e15-aab7-4632-85ce-321938cb096b|
|--------------------------------------------------------------------------------------------------------|||
|Ruta Archivo .ini||C:/Users/User/Desktop/noc/noc.ini|
|Proxies||{"http": "1.111.11.11:2323", "https": "1.111.11.11:2323"}|

### Obtener cola de trabajo de Forms
  
Obtiene las colas de trabajo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Asignar a variable|Variable donde guardar resultado sin {}|var|

### Obtener datos de Forms
  
Obtener datos de formulario de la cola de trabajo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID cola de trabajo|ID de la cola de trabajo|1|
|Form Token|Token del formulario|8YWUW8AXAV3UPNKY|

### Descarga archivo
  
Descarga un archivo subido a un formulario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID cola de trabajo|ID de la cola de trabajo|1|
|Archivo|Variable que tiene la ruta del archivo del formulario||
|Guardar archivo en|Ruta donde se guardará el archivo|C:\Rocketbot\file.ini|

### Actualizar estado de la cola Form
  
Cambia el estado de la cola
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Estado|Seleccione el estado de la cola||
|ID cola de trabajo|Ingrese el ID de la cola de trabajo|1|
|Asignar a variable|Nombre de variable sin {} donde se guardara el resultado||

### Devolver Mensaje a Xperience
  
Devuelve un mensaje al formulario Xperience
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token Xperience|Token de Xperience|{xperience}|
|Mensaje a devolver|Mensaje a devolver||
