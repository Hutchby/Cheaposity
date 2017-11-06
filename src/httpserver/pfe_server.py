#!/usr/bin/python

from server_base import RequestHandler
from http.server import HTTPServer

class PFEServer(HTTPServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.drone_battery = None
        self.drone_accel = None
        self.drone_gyro = None
        self.drone_magneto = None
        self.drone_gps = None
        pass

    def do_POST_gps(self, *args, **kwargs):
        self.drone_gps = kwargs['data']

    def do_POST_mpu(self, *args, **kwargs):
        self.drone_accel = kwargs['data']['accel']
        self.drone_gyro = kwargs['data']['gyro']
        self.drone_magneto = kwargs['data']['magneto']

    def do_POST_bat(self, *args, **kwargs):
        self.drone_battery = kwargs['data']

    def do_GET_status(self, *args, **kwargs):
        return {
                    'drone_state':
                    {
                        'battery': self.drone_battery,
                        'accel': self.drone_accel,
                        'gyro': self.drone_gyro,
                        'magneto': self.drone_magneto,
                        'gps': self.drone_gps,
                    },
               }


if __name__ == "__main__":
    server = PFEServer(("0.0.0.0", 8888), RequestHandler)
    server.serve_forever()
