FROM python:3.7.7-slim

ENV GROUP_NUM=24

#WORKDIR /app

RUN apt-get update && apt-get install -y git && apt-get install -y python3-pip

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

WORKDIR /practica_creativa2/bookinfo/src/productpage 

RUN pip install --no-cache-dir -r requirements.txt

RUN sed -i "s/<title>Simple Bookstore App<\/title>/<title>Grupo: 24<\/title>/" templates/productpage.html

EXPOSE 5060

CMD ["python3", "productpage_monolith.py"]