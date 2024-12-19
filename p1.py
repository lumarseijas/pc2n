#!/usr/bin/python3
from subprocess import call
import os
import sys

def arrancar(port_param='9080'):
    print("[DEBUG] Clonando el repositorio...")
    call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])

    print("[DEBUG] Actualizando paquetes e instalando dependencias...")
    call(['sudo', 'apt-get', 'update'])
    call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])

    print("[DEBUG] Navegando al directorio de la aplicación...")
    os.chdir('practica_creativa2/bookinfo/src/productpage')

    print("[DEBUG] Instalando las dependencias del proyecto...")
    call(['pip3', 'install', '-r', 'requirements.txt'])

    # Configurar variable de entorno
    os.environ['GROUP_NUM'] = '24'

    print("[DEBUG] Modificando el archivo productpage_monolith.py...")
    call(['mv', 'productpage_monolith.py', 'productpage_monolith_onlyRead.py'])

    with open('productpage_monolith_onlyRead.py', 'r') as fin, open('productpage_monolith.py', 'w') as fout:
        for line in fin:
            if 'flood_factor = 0 if (os.environ.get("FLOOD_FACTOR") is None)' in line:
                fout.write(line)
                fout.write(os.linesep + 'groupNumber = os.environ.get("GROUP_NUM", "Unknown")' + os.linesep)
            elif 'def front():' in line:
                fout.write(line)
                fout.write('    group = groupNumber' + os.linesep)
            elif '\'productpage.html\',' in line:
                fout.write(line)
                fout.write('    group=group,' + os.linesep)
            else:
                fout.write(line)

    print("[DEBUG] Eliminando archivo original temporal...")
    call(['rm', '-f', 'productpage_monolith_onlyRead.py'])

    print("[DEBUG] Modificando el archivo productpage.html...")
    os.chdir('templates')
    call(['mv', 'productpage.html', 'productpage_onlyRead.html'])

    with open('productpage_onlyRead.html', 'r') as fin, open('productpage.html', 'w') as fout:
        for line in fin:
            if '{% block title %}Simple Bookstore App{% endblock %}' in line:
                fout.write(line.replace(
                    '{% block title %}Simple Bookstore App{% endblock %}',
                    '{% block title %}GRUPO: {{ group }}{% endblock %}'
                ))
            else:
                fout.write(line)

    print("[DEBUG] Eliminando archivo HTML original temporal...")
    call(['rm', '-f', 'productpage_onlyRead.html'])

    print(f"[DEBUG] Arrancando la aplicación en el puerto {port_param}...")
    os.chdir('..')
    call(['python3', 'productpage_monolith.py', port_param])

def liberar():
    print("[DEBUG] Liberando recursos...")
    call(['rm', '-rf', 'practica_creativa2'])

param = sys.argv

if param[1] == "arrancarPuerto":
    arrancar(param[2])

if param[1] == "arrancar":
        arrancar()

if param[1] == "liberar":
    liberar()