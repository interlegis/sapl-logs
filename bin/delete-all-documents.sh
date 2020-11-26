#!/usr/bin/env bash

SOLR_URL=${1-'http://localhost:8983/solr'}

curl -X POST "$SOLR_URL/sapl-logs/update?commit=true" -H "Content-Type: text/xml" --data-binary '<delete><query>*:*</query></delete>'
