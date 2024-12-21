#!/usr/bin/python3
from subprocess import call
import os

# sudo apt-get -y update
# sudo apt-get -y upgrade
# sudo apt-get -y install git
# sudo apt-get -y install python3-pip
# sudo apt -y install docker.io
# sudo apt -y install docker-compose
# git clone --
# que construya las imagenes Docker para los servicios de productpage, details y ratings
# construir la imagen docker de reviews: docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
# construir 3 imagenes docker para diferentes versiones del servicio de reseñas:
# la primera muetra las reviews sin estrellas, la segunda con estrellas de color negro y la tercera con estrellas de color rojo.
# ejecutar los contenedores docker para todos los servicios

call('sudo apt-get update', shell=True)
call('yes | sudo apt-get upgrade', shell=True)
call("sudo apt-get -y install git", shell=True)
call("sudo apt-get -y install python3-pip", shell=True)
call("sudo apt -y install docker.io", shell=True)
call('sudo apt -y install docker compose', shell=True)
call('sudo chmod +x p3.py', shell=True)# + x--> permite ejecutar el archivo como programa

call('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git', shell=True)

#imagenes docker
#formato: nombreservicio/24
#call("sudo docker build -t NOMBREIMAGEN .")
call("docker build -t productpage/24 .", shell=True)
call("docker build -t details/24 .", shell=True)
call("docker build -t ratings/24 .", shell=True)

#comando (del enunciado) compilar y empaquetar ficheros necesarios ejecutando, dentro de src/reviews:
#hay q cambiar de directorio a /src/reviews?
call('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build', shell=True)

# añadir lo de las versiones de reviews
call ("docker build -t reviews-v1/24 -f ./reviews/Dockerfile --build-arg service_version=v1 --build-arg enable_ratings=false .", shell=True)
call ("docker build -t reviews-v2/24 -f ./reviews/Dockerfile --build-arg service_version=v2 --build-arg enable_ratings=true --build-arg star_color='black' .", shell=True)
call ("docker build -t reviews-v3/24 -f ./reviews/Dockerfile --build-arg service_version=v3 --build-arg enable_ratings=true --build-arg star_color='red' .", shell=True)

# call('sudo docker compose build', shell=True)
# call('sudo docker compose -f /home/upm/Desktop/pc2n/p3/docker-compose.yml up', shell=True)
call("docker compose up -d", shell=True)

