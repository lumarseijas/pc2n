MEMORIA PRÁCTICA CREATIVA 2
GRUPO 24: Cristina Rodríguez Lozano, Elsa Sastre del Olmo y Lucía Martínez Seijas
1. DESPLIEGUE DE LA APLICACIÓN EN MÁQUINA VIRTUAL PESADA
Para el despliegue de la aplicación como monolito, se desarrolló un script llamado p1.py que automatiza el proceso de instalación y configuración. Este script realiza las siguientes tareas:
1.	Actualización del sistema: Se asegura de que la máquina tenga los paquetes actualizados.
2.	Clonación del repositorio: Se clona el repositorio de la práctica que contiene el código de la aplicación.
3.	Instalación de dependencias: Se instalan las dependencias especificadas en el archivo requirements.txt del proyecto usando pip3.
4.	Personalización del título: Se configura la variable de entorno GROUP_NUM con el valor 24 y se modifica el archivo productpage.html para que el título de la aplicación incluya el número del grupo.
5.	Cambio de puerto de ejecución: La aplicación, que por defecto escucha en el puerto 9080, se ejecuta en un puerto configurable para adaptarse a diferentes configuraciones.
6.	Acceso externo: La aplicación es accesible desde cualquier navegador mediante la IP pública y el puerto configurado: http://<ip-pública>:<puerto>/productpage
7.	Liberación de recursos: Una vez terminada la ejecución, el script permite liberar recursos eliminando los archivos generados durante el proceso.
Para probar la funcionalidad, ejecutamos el script en la máquina con la IP local de nuestro ordenador. Utilizamos el comando: 
python3 p1.py arrancar
Y en nuestro navegador buscamos: http://<ip-local>:<puerto>/productpage
La aplicación muestra correctamente la interfaz gráfica con el título: “GRUPO 24”:


2. DESPLIEGUE DE UNA APLICACIÓN MONOLÍTICA USANDO DOCKER
Ahora queremos desplegar la misma aplicación monolítica utilizada en la P1, pero empleando contenedores Docker.
Para contenerizar la aplicación, definimos un fichero Dockerfile que:
o	Usa como base la imagen python:3.7.7-slim.
o	Instala dependencias necesarias como git y pip3.
o	Clona el repositorio con el código de la aplicación.
o	Configura la variable de entorno GROUP_NUM con el valor 24 para personalizar el título de la página.
o	Expone el puerto 5060 y ejecuta la aplicación.
Desarrollamos un script (p2.py) que automatiza el proceso de construcción y ejecución del contenedor Docker. Funciones:
o	Construcción de la imagen Docker usando el formato productpage/24.
o	Ejecución del contenedor con el nombre productpage-24, exponiendo el puerto 5060 y configurando la variable de entorno GROUP_NUM=24.
o	Liberación de recursos, deteniendo y eliminando contenedores e imágenes Docker.
El script fue ejecutado en una máquina local con Docker instalado, usando: python3 p2.py crear
En el navegador buscamos: http://<ip-local>:9080/productpage y muestra correctamente la interfaz gráfica con el título: "24"
 






3. SEGMENTACIÓN DE UNA APLICACIÓN MONOLÍTICA EN MICROSERVICIOS UTILIZANDO DOCKER-COMPOSE

