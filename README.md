#### Initial setup

1. Start solr in cloud mode:

    `$ sudo docker-compose up --build`

2. Upload configset sapl-logs:

    `$ bin/upload-config.sh`

3. Create collection:

    `$ bin/create-collection.sh`

4. Indexing files

    `$ python3 ./python-indexer/python-indexer.py logs/<log-file>`

5. Acessar UI
    `http://localhost:5000/search`
