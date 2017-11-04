#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import urllib.parse
import json
from pprint import pprint

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        rfile_len = int(self.headers['content-length'])
        self.post_data = self.rfile.read(rfile_len)
        qs = self.post_data.decode("utf-8")
        args = urllib.parse.parse_qs(qs)
        method = None
        for key in args.keys():
            try:
                method = getattr(self.server, "do_" + key)
            except e:
                method = None
                break
            method(self.server, data=args[key])
        if not method:
            self.send_response(501)
            self.send_header("content-type", "application/json")
            self.end_headers()
            error_message = "error: method not implemented"
            self.wfile.write(json.dumps(error_message).encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            message = "method: {} executed".format(method)
            self.wfile.write(json.dumps(message).encode("utf-8"))


class Server(HTTPServer, ThreadingMixIn):

    def do_print(self, *args, **kwargs):
        print(kwargs['data'])


if __name__ == "__main__":
    print("Launching HTTP server")
    server = Server(("0.0.0.0", 8888), RequestHandler)
    server.serve_forever()
