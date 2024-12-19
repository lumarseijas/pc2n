FROM node:12.18.1-slim

COPY practica_creativa2/bookinfo/src/ratings/package.json /opt/microservices/
COPY practica_creativa2/bookinfo/src/ratings/ratings.js /opt/microservices/

ENV SERVICE_VERSION=v1

RUN npm install

ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

EXPOSE 9080

CMD ["node","/opt/microservices/ratings.js", "9080"]