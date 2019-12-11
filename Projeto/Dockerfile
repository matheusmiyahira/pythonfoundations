FROM python:3.6.8-alpine

LABEL author = Daniel Silva

LABEL version = 1.0

WORKDIR /Projeto

COPY . .

RUN apt update && apt install pipenv && pipenv install -r requirements.txt

EXPOSE 5000

RUN ["flask","run"]