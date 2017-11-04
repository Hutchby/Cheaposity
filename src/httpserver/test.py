#!/usr/bin/python

import requests

if __name__ == "__main__":
    # This request is supposed to work well with the server
    post_data = {'print': 'Test message'}
    r = requests.post("http://0.0.0.0:8888", data=post_data)
    print(r.text)
