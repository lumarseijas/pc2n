FROM ruby:2.7.1-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

WORKDIR /practica_creativa2/bookinfo/src/details

COPY /details.rb /opt/microservices/

ARG service_version
ARG enable_external_book_service
ENV SERVICE_VERSION ${service_version:-v1}
ENV ENABLE_EXTERNAL_BOOK_SERVICE ${enable_external_book_service:-true}

EXPOSE 9080

CMD ["ruby", "details.rb", "9080"]
