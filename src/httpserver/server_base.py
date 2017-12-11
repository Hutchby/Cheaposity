#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import urllib.parse
from urllib.parse import unquote
import json
from pprint import pprint

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        rfile_len = int(self.headers['content-length'])
        self.post_data = self.rfile.read(rfile_len)
        qs = self.post_data.decode("utf-8")
        qs = unquote(qs)
        args = json.loads(qs)
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
            method_data = args[key]
            try:
                method(self.server, data=method_data)
            except Exception as e:
                print(e)
                print(method_data)
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

    def do_GET(self):
        try:
            self.path = unquote(self.path)
            path = self.path.split("?")
            path[0] = path[0][1:]
            method = getattr(self.server, "do_GET_" + path[0])
            if len(path) > 1:
                method_kwargs = dict(urllib.parse.parse_qsl(path[1]))
            else:
                method_kwargs = {}
        except Exception as e:
            print(e)
            self.send_response(501)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        response = method(self.server, **method_kwargs)
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))


class PrintServer(HTTPServer, ThreadingMixIn):

    def do_POST_print(self, *args, **kwargs):
        print(kwargs)

    def do_GET_status(self, *args, **kwargs):
        print(kwargs)

if __name__ == "__main__":
    print("Launching HTTP server")
    server = PrintServer(("0.0.0.0", 8888), RequestHandler)
    server.serve_forever()
