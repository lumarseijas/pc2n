FROM node:12.18.1-slim

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

COPY ./package.json /opt/microservices/

COPY ./ratings.js /opt/microservices/

WORKDIR /opt/microservices

RUN npm install

ARG service_version
ENV SERVICE_VERSION ${service_version:-v1}

EXPOSE 9080

CMD ["node","ratings.js", "9080"]