#!/usr/bin/python3
import os
import sys
from subprocess import call

# Actualizar el sistema e instalar Docker

call(["sudo apt-get -y update "], shell=True)
call(["sudo apt-get -y install docker.io "], shell=True)
def crear():
    # Crear la imagen de Docker
    print("[DEBUG] Construyendo la imagen de Docker...")
    call("sudo docker build -t productpage/24 . ", shell=True)
    # Ejecutar el contenedor
    print("[DEBUG] Ejecutando el contenedor de Docker...")
    call("sudo docker run --name productpage-24 -p 5060:5060 -e GROUP_NUM=24 -d productpage/24", shell=True)  
    print("[DEBUG] Contenedor ejecutándose en el puerto 5060.")
   

from subprocess import call

def liberar():
    print("[DEBUG] Liberando recursos...")
    # Detener y eliminar el contenedor
    call("sudo docker stop product-page-g24", shell=True)
    call("sudo docker rm product-page-g24", shell=True)
    call("sudo docker rmi -f product-page/g24", shell=True)
    print("[INFO] Contenedor y recursos eliminados correctamente.")

comando = sys.argv[1]

if comando == "crear":
    crear()
elif comando == "liberar":
    liberar()