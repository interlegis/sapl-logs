#!/usr/bin/env bash

SOLR_URL=${1-'http://localhost:8983/solr'}

curl -X POST "$SOLR_URL/sapl-logs/update?commit=true&stream.body=<delete><query>*%3A*</query></delete>"
