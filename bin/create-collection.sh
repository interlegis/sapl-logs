#!/usr/bin/env bash

SOLR_URL=${1-'http://localhost:8983/solr'}
curl -X POST "$SOLR_URL/admin/collections?action=CREATE&name=sapl-logs&numShards=2&replicationFactor=1&collection.configName=sapl-logs"
