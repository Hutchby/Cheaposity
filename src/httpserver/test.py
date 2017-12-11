#!/usr/bin/python

import requests
import json
from pprint import pprint

SERVER_ADDR = 'http://0.0.0.0:8888/'

REQUESTS = [
        (requests.post, '', {'bat': 100}),
        (requests.post, '', {'gps': 'Test with string'}),
        (requests.post, '', {'mpu': {'accel': 10, 'gyro': 15, 'magneto': 20},}),
        (requests.get, 'status', {}),
        ]

if __name__ == "__main__":
    # This request is supposed to work well with the server
    for rq in REQUESTS:
        r = rq[0](SERVER_ADDR + rq[1], data=json.dumps(rq[2]))
        pprint(json.loads(r.text))
