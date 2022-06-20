# syntax=docker/dockerfile:1
FROM python:3.10.5-alpine3.16

RUN mkdir -p /api
WORKDIR /api
ADD . .
RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=25005

EXPOSE 25005
CMD ["flask", "run"]