FROM python:3.7.7-slim

EXPOSE 5080

ENV GROUP_NUM=24

#WORKDIR /app

RUN apt-get update && apt-get install -y git && apt-get install -y python3-pip

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

WORKDIR /practica_creativa2/bookinfo/src/productpage 

RUN pip3 install -r requirements.txt

RUN sed -i "s/Simple\sBookstore\sApp/${GROUP_NUM}/g" templates/productpage.html

CMD ["python3", "productpage_monolith.py", "5080"]