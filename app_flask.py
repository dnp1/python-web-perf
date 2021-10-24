from os import environ

import flask
import json

from sync_db import get_row

if environ.get('GEVENT') == '1':
    import psycogreen.gevent

    psycogreen.gevent.patch_psycopg()

app = flask.Flask("python-web-perf")

pool = None


@app.route("/test")
def test():
    a, b = get_row()
    return json.dumps({
                          "a": str(a).zfill(10),
                          "b": b
                      })
