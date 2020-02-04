#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2020 Nichole Mattera
#

import serial
from flask import request
from app.views.serial_method_view import SerialMethodView
from app.models.serial_requests import createTie, getTie
from app.models.responses import ErrorResponse, TieResponse

class TieIDView(SerialMethodView):
    def get(self, output):
        if output < 1 or output > 8:
            return ErrorResponse(4, 'Output field is out of range.').response(500)
        
        try:
            s = self.connect()
            s.write(getTie(output))
            return TieResponse(s.readline(), output).response(200)
        except serial.serialutil.SerialException as e:
            return ErrorResponse(0, 'Device not available.').response(500)

    def delete(self, output):
        if output < 1 or output > 8:
            return Error(4, 'Output field is out of range.').response(500)

        try:
            s = self.connect()
            s.write(createTie(0, output))
            return TieResponse(s.readline()).response(200)
        except serial.serialutil.SerialException as e:
            return Error(0, 'Device not available.').response(500)

class TieView(SerialMethodView):
    def post(self):
        data = request.json

        if 'input' not in data:
            return Error(1, 'Input field is required.').response(500)
        if 'output' not in data:
            return Error(2, 'Output field is required.').response(500)
        if data['input'] < 1 or data['input'] > 12:
            return Error(3, 'Input field is out of range.').response(500)
        if data['output'] < 1 or data['output'] > 8:
            return Error(4, 'Output field is out of range.').response(500)

        try:
            s = self.connect()
            s.write(createTie(data['input'], data['output']))
            return TieResponse(s.readline()).response(200)
        except serial.serialutil.SerialException as e:
            return Error(0, 'Device not available.').response(500)
