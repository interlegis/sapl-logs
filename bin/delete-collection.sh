#!/usr/bin/env bash

SOLR_URL=${1-'http://localhost:8983/solr'}

curl -X POST "$SOLR_URL/admin/collections?action=DELETE&name=sapl-logs"
