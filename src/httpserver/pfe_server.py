#!/usr/bin/python

from server_base import RequestHandler

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
        self.drone_gps = kwargs['data'][0]

    def do_POST_mpu(self, *args, **kwargs):
        self.drone_accel = kwargs['data'][0]['accel']
        self.drone_gyro = kwargs['data'][0]['gyro']
        self.drone_magneto = kwargs['data'][0]['magneto']

    def do_POST_bat(self, *args, **kwargs):
        self.drone_battery = kwargs['data'][0]
