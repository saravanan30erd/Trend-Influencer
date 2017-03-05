FROM ubuntu:latest
MAINTAINER Saravanan

RUN apt-get update \
    && apt-get install python python-pip -y \	
    && pip install pymongo flask

WORKDIR /mnt/web

CMD python app.py
