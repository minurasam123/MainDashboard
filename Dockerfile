FROM python:3.8-alpine
MAINTAINER London App Developer Ltd

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /elearningDash
WORKDIR /elearningDash
COPY ./elearningDash /elearningDash

RUN adduser -D user
USER user
