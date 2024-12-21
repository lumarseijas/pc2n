#!/usr/bin/python3
import os
import sys
from subprocess import call

# Actualizar el sistema e instalar Docker
#call(["sudo", "apt", "update"])
#call(["sudo", "apt", "install", "-y", "docker.io"])
call(["sudo apt-get -y update "], shell=True)
call(["sudo apt -y install docker.io "], shell=True)
def crear():
    # Crear la imagen de Docker
    print("[DEBUG] Construyendo la imagen de Docker...")
    call("sudo docker build -t product-page/24 . ")
    # Ejecutar el contenedor
    print("[DEBUG] Ejecutando el contenedor de Docker...")
    call("sudo docker run --name g24-product-page -p 5060:5060 -e GROUP_NUM=24 -d product-page/24")  
    print("[DEBUG] Contenedor ejecutándose en el puerto 5060.")
   

from subprocess import call

def liberar():
    print("[DEBUG] Liberando recursos...")
    # Detener y eliminar el contenedor
    call(["sudo", "docker", "stop", "product-page-g24"])
    call(["sudo", "docker", "rm", "product-page-g24"])
    call(["sudo", "docker", "rmi", "-f", "product-page/24"])
    print("[INFO] Contenedor y recursos eliminados correctamente.")

comando = sys.argv[1]

if comando == "crear":
    crear()
elif comando == "liberar":
    liberar()