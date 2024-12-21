FROM ruby:2.7.1-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

WORKDIR /practica_creativa2/bookinfo/src/details

#dependencias de ruby:
RUN gem install bundler && bundle install 

COPY /details.rb /opt/microservices/

ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

EXPOSE 9080

CMD ["ruby", "details.rb", "9080"]
