#!/usr/bin/python3
from subprocess import call
import os
import sys

# ERROR AL CREAR LOS SERVICIOS RATINGS, DETAILS Y REVIEWS, PRODUCTPAGE LO HACE BIEN

def crear():
    call('sudo apt-get update', shell=True)
    call("sudo apt-get install -y containerd", shell=True)
    call("sudo apt-get install -f", shell=True) #nueva
    call('yes | sudo apt-get upgrade', shell=True)
    call('yes | sudo apt-get install -y git python3-pip docker.io docker-compose', shell=True)

    call('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git', shell=True)

    #imagenes docker
    #formato: nombreservicio/24
    #call("sudo docker build -t NOMBREIMAGEN .")
    call("docker build -t productpage/24 ./productpage/Dockerfile .", shell=True) #he cambiado que sea en vez de . ./productpage/Dockerfile . (en los 3 servicios)
    call("docker build -t details/24 ./details/Dockerfile .", shell=True)
    call("docker build -t ratings/24 ./ratings/Dockerfile .", shell=True)

    #comando (del enunciado) compilar y empaquetar ficheros necesarios ejecutando, dentro de src/reviews:
    #cambiar de directorio a /src/reviews
    os.chdir("practica_creativa2/bookinfo/src/reviews")
    call('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build', shell=True)

    # añadir lo de las versiones de reviews
    call ("docker build -t reviews-v1/24 -f ./reviews/Dockerfile --build-arg service_version=v1 --build-arg enable_ratings=false .", shell=True)
    call ("docker build -t reviews-v2/24 -f ./reviews/Dockerfile --build-arg service_version=v2 --build-arg enable_ratings=true --build-arg star_color='black' .", shell=True)
    call ("docker build -t reviews-v3/24 -f ./reviews/Dockerfile --build-arg service_version=v3 --build-arg enable_ratings=true --build-arg star_color='red' .", shell=True)

    call("docker compose up --build -d", shell=True)

def liberar():
    call("docker compose down", shell=True)
    call("docker rmi -f $(docker images -q)", shell=True)
    call("sudo rm -rf practica_creativa2", shell=True)

comando = sys.argv[1]

if comando == "crear":
    crear()
elif comando == "liberar":
    liberar()