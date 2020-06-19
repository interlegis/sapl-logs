

#### Initial setup

__Make sure you have the env variable $SOLR_HOME setup__

1. Start solr in cloud mode:

`$SOLR_HOME/bin/solr start -c`

2. Upload configset sapl-logs:

`./bin/upload-config.sh`

3. Create collection:

`./bin/create-collection.sh`

#### Indexing files

1. `./python-indexer/python-indexer.sh logs/<log-file>`

### Starting Flask app

1. `./bin/run-flask`
