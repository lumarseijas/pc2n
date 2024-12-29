FROM ruby:2.7.1-slim

# Crear el directorio donde se alojará el archivo details.rb
WORKDIR /opt/microservices

# Clonar el repositorio y copiar el archivo details.rb
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/CDPS-ETSIT/practica_creativa2.git /repo && \
    cp /repo/bookinfo/src/details/details.rb /opt/microservices/

# Establecer las variables de entorno
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

# Exponer el puerto 9080
EXPOSE 9080

# Ejecutar el archivo details.rb
CMD ["ruby", "details.rb", "9080"]
