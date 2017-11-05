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
        errors = []
        messages = []
        for key in args.keys():
            try:
                method = getattr(self.server, "do_POST_" + key)
                message = "method: {} executed".format("do_POST_" + key)
                messages.append(message)
            except Exception:
                error_message = "error: method {} not implemented".format("do_POST_" + key)
                errors.append(error_message)
                continue
            method(self.server, data=args[key])
        if errors:
            self.send_response(501)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(errors).encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
        self.wfile.write(json.dumps(messages).encode("utf-8"))


class PrintServer(HTTPServer, ThreadingMixIn):

    def do_POST_print(self, *args, **kwargs):
        print(kwargs['data'][0])


if __name__ == "__main__":
    print("Launching HTTP server")
    server = PrintServer(("0.0.0.0", 8888), RequestHandler)
    server.serve_forever()
