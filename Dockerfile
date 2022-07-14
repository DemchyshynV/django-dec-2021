FROM python:3.10-alpine

MAINTAINER Me

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache --virtual ..build-deps gcc musl-dev mariadb-dev
#for Pillow
RUN apk add jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN adduser -D user
RUN chown -R user:user /app
USER user

ENV PATH="/home/user/.local/bin:${PATH}"

COPY ./Pipfile /tmp/

RUN cd /tmp \
    && pip install --upgrade pip\
    && pip install --user pipenv\
    && pipenv lock --requirements > requirements.txt\
    && pip install --user -r requirements.txt


