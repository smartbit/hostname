#!/usr/bin/env python
import socket
import os
import statsd

from flask import Flask
app = Flask(__name__)
c = statsd.StatsClient('localhost', 8125)

@app.route('/')
def hello_world():
    s = 'Hostname is: ' + socket.gethostname()
    c.incr('hits')
    return s

MYPORT = int(os.environ.get("PORT0", "0"))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=MYPORT)
