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

#os.chdir('practica_creativa2/bookinfo/src/reviews')
call('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build', shell=True)

call('sudo docker compose build', shell=True)
call('sudo docker compose -f /home/upm/Desktop/pc2n/p3/docker-compose.yml up', shell=True)

