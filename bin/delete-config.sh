#!/usr/bin/env bash

SOLR_URL=${1-'http://localhost:8983/solr'}

curl -X POST "$SOLR_URL/admin/configs?action=DELETE&name=sapl-logs&omitHeader=true"
