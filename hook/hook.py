#!/usr/bin/env python

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/',methods=['POST'])
def hook():
    return request.data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
