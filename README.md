#### Initial setup

1. Start solr in cloud mode:

    `$ sudo docker-compose up"`

2. Upload configset sapl-logs:

    `$ bin/upload-config.sh`

3. Create collection:

    `$ bin/create-collection.sh`

4. Indexing files

    `$ ./python-indexer/python-indexer.sh logs/<log-file>`