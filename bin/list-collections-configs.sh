#!/usr/bin/env bash
SOLR_URL=${1-'http://localhost:8983/solr'}

curl -X GET "$SOLR_URL/admin/collections?action=LIST"

curl -X GET "$SOLR_URL/admin/configs?action=LIST"
