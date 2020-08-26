FROM python:3.8-alpine

RUN apk update;\
    apk upgrade;\
    apk add bash curl nano zip

WORKDIR /var/interlegis/sapl-logs

COPY requirements.txt ./
COPY log-inspector/ log-inspector/
COPY python-indexer/ python-indexer/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python log-inspector/log-inspector.py
