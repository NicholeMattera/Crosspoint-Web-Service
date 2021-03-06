#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2020 Nichole Mattera
#

from app.views.serial_method_view import SerialMethodView
from app.models.serial_requests import infoRequest
from app.models.responses import ErrorResponse, InfoResponse
import serial

class InfoView(SerialMethodView):
    def get(self):
        try:
            s = self.connect()
            s.write(infoRequest())
            return InfoResponse(s.readline()).response(200)
        except serial.serialutil.SerialException as e:
            return ErrorResponse(0, 'Device not available.').response(500)
