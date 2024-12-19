#!usr/bin/python3
from subprocess import call
import os


os.system('sudo apt-get update')
os.system('yes | sudo apt-get upgrade')
os.system('sudo apt install docker-compose')
os.system('sudo chmod +x /usr/local/bin/docker-compose')# + x--> permite ejecutar el archivo como programa


os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
os.chdir('practica_creativa2/bookinfo/src/reviews')
os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
os.chdir(os.path.expanduser("~")) #??

os.system('sudo docker-compose build')
os.system('sudo docker-compose -f /home/upm/prueba2/bloque3/compose.yaml up')