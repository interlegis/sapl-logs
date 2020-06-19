#!/usr/bin/env bash

if [[ -z $SOLR_HOME ]]; then
  echo 'Cannot run script! You need to setup $SOLR_HOME'
  exit
fi

$SOLR_HOME/bin/solr zk upconfig -n sapl-log -d solr/sapl-logs/ -z localhost:9983
