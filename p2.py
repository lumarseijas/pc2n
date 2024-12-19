#!/usr/bin/python3
import os
import sys
from subprocess import run, CalledProcessError

def crear_dockerfile():
    print("[DEBUG] Creando archivo Dockerfile...")
    dockerfile_content = """
    FROM python:3.7.7-slim

    # Configuración de la variable de entorno
    ENV GROUP_NUM=24

    # Instalar dependencias necesarias
    RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

    # Clonar el repositorio de la aplicación
    RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

    # Navegar al directorio de la aplicación
    WORKDIR /practica_creativa2/bookinfo/src/productpage

    # Instalar las dependencias de Python
    RUN pip3 install -r requirements.txt

    # Exponer el puerto donde correrá la aplicación
    EXPOSE 5060

    # Comando para ejecutar la aplicación
    CMD ["python3", "productpage_monolith.py", "5060"]
    """
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    print("[DEBUG] Dockerfile creado correctamente.")

def crear():
    try:
        # Crear el Dockerfile
        crear_dockerfile()

        # Crear la imagen de Docker
        print("[DEBUG] Construyendo la imagen de Docker...")
        os.system("sudo docker build -t product-page/g24 . ")

        # Ejecutar el contenedor
        print("[DEBUG] Ejecutando el contenedor de Docker...")
        os.system("sudo docker run --name product-page-g24 -p 5060:5060 -e GROUP_NUM=24 -d product-page/g24")  

        print("[DEBUG] Contenedor ejecutándose en el puerto 5060.")
    except CalledProcessError as e:
        print(f"[ERROR] Error durante la ejecución: {e}")
        liberar()

def liberar():
    print("[DEBUG] Liberando recursos...")
    try:
        # Detener y eliminar el contenedor
        run(["sudo","docker", "stop", "product-page-g24"], check=True)
        run(["sudo", "docker", "rm", "product-page-g24"], check=True)
    except CalledProcessError:
        print("[INFO] No se encontró un contenedor en ejecución.")

    try:
        # Eliminar la imagen de Docker
        run(["sudo","docker", "rmi", "-f", "product-page/g24"], check=True)
    except CalledProcessError:
        print("[INFO] No se encontró una imagen para eliminar.")

    # Eliminar el archivo Dockerfile
    if os.path.exists("Dockerfile"):
        os.remove("Dockerfile")
        print("[DEBUG] Archivo Dockerfile eliminado.")
    else:
        print("[INFO] No se encontró un archivo Dockerfile.")

comando = sys.argv[1]

if comando == "crear":
    crear()
elif comando == "liberar":
    liberar()