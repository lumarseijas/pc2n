FROM python:3.7.7-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y git && apt-get clean
RUN apt-get install -y python3-pip

# Clonar el repositorio
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git 

# Copiar el archivo requirements.txt y productpage.py al contenedor
WORKDIR /practica_creativa2/bookinfo/src/productpage
# Instalar las dependencias del archivo requirements.txt
RUN pip install flask

RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto usado por la aplicación
EXPOSE 9080

#añado el numero de grupo
ENV GROUP_NUMBER=24

# Ejecutar la aplicación
CMD ["python3", "productpage.py", "9080"]
