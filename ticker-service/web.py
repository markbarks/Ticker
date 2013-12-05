from Queue import Queue
import json
import threading

import random
from flask import Flask
from flask.ext.sockets import Sockets
import time


app = Flask(__name__)
sockets = Sockets(app)

q = Queue()


@sockets.route('/receive')
def outbox(ws):
    while ws is not None:
        item = q.get(block=True)
        ws.send(item)


def mock_trade_source():
    while True:
        trade = dict(market='Eurex V', feedcode='OESXC201009001000',
                     price=random.uniform(2357, 2358),
                     volume=random.randint(100, 400), buysell="buy", currency='USD')
        print json.dumps(trade)
        q.put(json.dumps(trade))
        time.sleep(random.randint(1,5))


def start_consumer():
    t = threading.Thread(target=mock_trade_source)
    t.setDaemon(True)
    t.start()


consumer_thread = start_consumer()
