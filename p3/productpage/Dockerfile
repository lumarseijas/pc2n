FROM python:3.7.7-slim

ENV GROUP_NAME=24

RUN apt-get update && apt-get install -y git 

RUN apt-get update
#el unico que no he puesto ha sido el upgrade
RUN apt-get install -y python3-pip

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

WORKDIR /practica_creativa2/bookinfo/src/productpage

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "productpage.py", "9080" ]
