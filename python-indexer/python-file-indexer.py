#!/usr/bin/env python
import sys

SOLR_URL='http://localhost:8983/solr'

def parse_logs(filename):
    import re
    import json
    import requests
    PAT = '^(ERROR|INFO|DEBUG\WARN)\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2},\d+)\s+(.*)'

    with open(filename, 'r') as f:
        lines = f.readlines()
        previous = None
        buffer = []
        payload = []
        for l in lines:
            match = re.match(PAT, l)
            if match:

                if buffer and previous:
                    previous['stacktrace'] = ''.join(buffer)
                    # print(previous)
                    # payload.append(previous)
                    buffer.clear()
                elif not previous:
                    buffer.clear()

                groups = match.groups()

                datetime = groups[1] + "T" + groups[2].split(',')[0] + "Z"

                fields = {
                    'level': groups[0],
                    'datetime': datetime,
                    'line': l,
                }

                parts = groups[3].split()
                fields['server'] = parts[0]
                fields['path'] = parts[1]
                
                # sapl.painel.views:get_votos:497
                function = parts[2].split(':')
                fields['app_file'] = function[0]
                fields['method'] = function[1]
                fields['line_number'] = function[2]

                fields['function'] = parts[2]

                fields['message'] = ' '.join(parts[3:])

                if previous:
                    payload.append(previous)

                previous = fields

                # print(fields)
                # payload.append({
                #     'add': {
                #         'commitWithin': 1000,
                #         'doc': fields,
                #     }
                # })
                # payload.append(fields)

            else:
                buffer.append(l)
        if buffer and previous:
            previous['stacktrace'] = ''.join(buffer)
            # print(previous)
            buffer.clear()
            payload.append(previous) # Need this one???

        print(len(payload))

        # Push to Solr
        r = requests.post('http://localhost:8983/solr/sapl-logs/update?commitWithin=1000',
                          data=json.dumps(payload),
                          headers={'Content-Type': 'application/json; charset=utf-8'}
                          )
        print(r.content)


if __name__ == '__main__':
    parse_logs(sys.argv[1])
