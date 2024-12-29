#!/usr/bin/python3
from subprocess import call
import os
import sys

# ERROR AL CREAR LOS SERVICIOS RATINGS, DETAILS Y REVIEWS, PRODUCTPAGE LO HACE BIEN

def crear():
    
    call('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git', shell=True)

    #imagenes docker
    #formato: nombreservicio/24
    #call("sudo docker build -t NOMBREIMAGEN .")
    call("docker compose build", shell=True)
    
    #comando (del enunciado) compilar y empaquetar ficheros necesarios ejecutando, dentro de src/reviews:
    #cambiar de directorio a /src/reviews
    os.chdir("practica_creativa2/bookinfo/src/reviews")
    call('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build', shell=True)
    os.chdir("../..")
    # añadir lo de las versiones de reviews
    call("docker build --build-arg service_version=v1 --build-arg enable_ratings=false --build-arg star_color=black -t reviews/24:v1 practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/", shell=True)
    call("docker build --build-arg service_version=v2 --build-arg enable_ratings=true --build-arg star_color=black -t reviews/24:v2 practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/", shell=True)
    call("docker build --build-arg service_version=v3 --build-arg enable_ratings=true --build-arg star_color=red -t reviews/24:v3 practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/", shell=True)
    
    call("docker compose up --build", shell=True)
    call("docker compose up -d", shell=True)

def liberar():
    call("docker compose down", shell=True)
    call("docker rmi -f $(docker images -q)", shell=True)
    call("sudo rm -rf practica_creativa2", shell=True)

comando = sys.argv[1]

if comando == "crear":
    crear()
elif comando == "liberar":
    liberar()