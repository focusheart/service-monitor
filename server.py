# -*- coding:utf8 -*-

import datetime
import json
import codecs
from flask import Flask, request, session, g, redirect, url_for, \
  abort, render_template, flash, jsonify, send_from_directory

DEBUG = True
FMT_DATETIME = '%Y-%m-%d %H:%M:%S'
SECRET_KEY = 'development skey'
HOST = '0.0.0.0'
PORT = 50303

# service configs
SERVICE_LIST = json.loads(codecs.open('services.json', 'r', 'utf8').read())
SERVICE_KEYS = [s['skey'] for s in SERVICE_LIST]
SERVICE_DICT = dict(zip(SERVICE_KEYS, SERVICE_LIST))

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    '''
    Homepage of monitor service
    '''
    return render_template('index.html', services=SERVICE_LIST)


@app.route('/chk/<skey>')
def chk(skey):
    '''
    Check service status of specific skey
    '''
    if skey not in SERVICE_KEYS:
        return jsonify({'success':False, 'msg':'No such service'})

    service = SERVICE_DICT[skey]

    # check the service status here

    # update status
    status = 'RUNNING'

    ret = {
        'success': True,
        'datetime': datetime.datetime.now().strftime(FMT_DATETIME),
        'msg': 'Service %s is %s' % (skey, status)
    }

    return jsonify(ret)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)        
