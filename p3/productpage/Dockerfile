FROM python:3.7.7-slim

RUN apt-get update && apt-get install -y git 

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

RUN apt-update
RUN apt-get install -y python3-pip

WORKDIR /practica_creativa2/bookinfo/src/productpage

RUN pip3 install requirements.txt

CMD [ "python3", "productpage.py", "9080" ]
