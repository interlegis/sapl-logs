#!/usr/bin/env bash

SOLR_URL=${1-'http://localhost:8983/solr'}

# zip configset sapl-logs
cd ./solr/sapl-logs/conf && zip -r sapl-logs.zip .

curl -X POST --header "Content-Type:application/octet-stream" --data-binary @sapl-logs.zip "$SOLR_URL/admin/configs?action=UPLOAD&name=sapl-logs"

#rm sapl-logs.zip
cd -
