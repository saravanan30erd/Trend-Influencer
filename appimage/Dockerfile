FROM ubuntu:latest
MAINTAINER Saravanan

RUN apt-get update \
	&& apt-get install python python-pip -y \
	&& pip install pymongo tweepy

WORKDIR /mnt/app

CMD python influencer.py
