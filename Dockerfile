FROM python:3.8-alpine

RUN apk update;\
    apk upgrade;\
    apk add bash;\
    apk add curl;\
    apk add zip

WORKDIR /usr/src/app

ADD . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

VOLUME ["/usr/src/app"]

CMD ["/usr/src/app/bin/run-flask.sh"]
