FROM python:3.8-alpine

RUN apk update;\
    apk upgrade;\
    apk add bash;\
    apk add curl;\
    apk add zip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000