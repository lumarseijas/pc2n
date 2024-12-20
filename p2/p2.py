#!/usr/bin/python3
import os
import sys
from subprocess import call

call('sudo', 'apt', 'update')
call('sudo', 'apt', 'install', 'docker.io')
def crear():
    # Crear la imagen de Docker
    print("[DEBUG] Construyendo la imagen de Docker...")
    os.system("sudo docker build -t product-page/g24 . ")
    # Ejecutar el contenedor
    print("[DEBUG] Ejecutando el contenedor de Docker...")
    os.system("sudo docker run --name product-page-g24 -p 5060:5060 -e GROUP_NUM=24 -d product-page/g24")  
    print("[DEBUG] Contenedor ejecutándose en el puerto 5060.")
   

def liberar():
    print("[DEBUG] Liberando recursos...")
    # Detener y eliminar el contenedor
    call("sudo","docker", "stop", "product-page-g24")
    call("sudo", "docker", "rm", "product-page-g24")
    call("sudo","docker", "rmi", "-f", "product-page/g24")
    print("[INFO] No se encontró una imagen para eliminar.")

comando = sys.argv[1]

if comando == "crear":
    crear()
elif comando == "liberar":
    liberar()