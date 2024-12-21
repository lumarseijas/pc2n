FROM openliberty/open-liberty:full-java11-openj9-ubi

# Copiar la aplicación empaquetada al contenedor
COPY build/libs/reviews-1.0.0.jar /config/dropins/

# Configuración de variables de entorno
ENV SERVICE_VERSION=v1
ENV ENABLE_RATINGS=true
ENV STAR_COLOR=black

# Exponer el puerto para el servicio
EXPOSE 9080

# Comando para arrancar Open Liberty
CMD ["/opt/ol/wlp/bin/server", "run", "defaultServer"]
