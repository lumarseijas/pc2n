FROM node:16-slim

WORKDIR /opt/microservices

# Instalar git
RUN apt-get update && apt-get install -y git && apt-get clean

# Clonar el repositorio
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git /repo

# Copiar los archivos necesarios
RUN cp /repo/bookinfo/src/ratings/package.json /opt/microservices/
RUN cp /repo/bookinfo/src/ratings/ratings.js /opt/microservices/

# Establecer la variable de entorno
ENV SERVICE_VERSION=v1 

# Instalar las dependencias
RUN npm install

# Exponer el puerto 9080
EXPOSE 9080

# Ejecutar el archivo ratings.js
CMD ["node", "ratings.js", "9080"]
