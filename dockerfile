# syntax=docker/dockerfile:1
FROM python:3.10.5-alpine3.16

RUN mkdir -p /api
WORKDIR /api
RUN mkdir -p basicwebapi
ADD basicwebapi basicwebapi
ADD requirements.txt .
RUN pip install -r requirements.txt

ENV FLASK_APP=basicwebapi
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=25005

RUN flask init-db

EXPOSE 25005
CMD ["flask", "run"]