

#### Initial setup

__Make sure you have the env variable $SOLR_HOME setup__

1. Start solr in cloud mode:

`sudo docker run -p 8983:8983 -p 9983:9983 -it solr:7.7.3 bash -c "bin/solr start -f -c"`

2. Upload configset sapl-logs:

`./bin/upload-config.sh`

3. Create collection:

`./bin/create-collection.sh`

#### Indexing files

1. `./python-indexer/python-indexer.sh logs/<log-file>`

### Starting Flask app

1. `./bin/run-flask`
