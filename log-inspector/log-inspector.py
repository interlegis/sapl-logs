from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, emit
import requests
import os


app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.jinja_env.filters['zip'] = zip

app.debug = True

SOLR_URL = os.getenv('SOLR_URL', 'http://localhost:8983/solr/sapl-logs/select')

FQ_PARAMS = "facet=true" \
            "&facet.mincount=1" \
            "&facet.field=level" \
            "&facet.field=server" \
            "&facet.field=app_file" \
            "&facet.range=datetime" \
            "&facet.range.start=NOW/DAY%2D7DAYS" \
            "&facet.range.end=NOW/DAY" \
            "&facet.range.gap=%2B1DAY" \



@app.route('/', methods=['GET', 'POST'])
def search():
    q = request.args.get('q', '')
    rows = request.args.get('rows', '10')
    as_json = request.args.get('as_json', False)


    # monta fq
    filter_queries = request.args.getlist('fq')
    filters = ''
    if filter_queries:
        for f in filter_queries:
            filters += '&fq=' + f

    facets = FQ_PARAMS
    SOLR = f"{SOLR_URL}?q={q}&wt=json&{facets}&{filters}&rows={rows}"
    resp = requests.get(SOLR)
    try:
        result = resp.json()
    except Exception as e:
        print(resp.content)
        return e

    if as_json:
        return jsonify(result)
    else:
        return render_template('index.html',
                               result=result,
                               q=q,
                               rows=rows,
                               filters=filters)


@app.route('/analytics', methods=['GET'])
def analytics():
    return render_template('analytics.html')


@app.route('/stream', methods=['GET'])
def stream():
    # requests.post('http://localhost:8983/solr/sapl-logs/stream', data='expr=search(sapl-logs, q="*:*")').content
    payload = {'expr': 'search(sapl-logs, q="*:*", qt="/export", fl="datetime, level, id", sort="datetime asc")'}
    r = requests.get('http://localhost:8983/solr/sapl-logs/stream', data=payload, stream=True)
    return r.json()

    # for c in r.iter_lines():
    #     ...: print(c)
    # return jsonify({'message': 'hello, world!'})

if __name__=='__main__':
    app.run(host='0.0.0.0')
