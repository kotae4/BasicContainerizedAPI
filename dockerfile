# syntax=docker/dockerfile:1
FROM python:3.9-buster

RUN mkdir -p /api
WORKDIR /api
RUN mkdir -p basicwebapi

ADD basicwebapi basicwebapi
ADD requirements.txt .
ADD basicwebapi-settings.cfg .
ADD bootstrap.sh .
RUN chmod 777 bootstrap.sh

RUN apt-get install libmariadb3 libmariadb-dev
RUN pip install -r requirements.txt