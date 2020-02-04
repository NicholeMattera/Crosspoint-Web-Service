#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2020 Nichole Mattera
#

import serial

config = {
    'totalNumberOfOutputs': 8,
    'totalNumberOfInputs': 12,
    'device': '/dev/ttyUSB0',
    'baudrate': 9600,
    'bytesize': serial.EIGHTBITS,
    'parity': serial.PARITY_NONE,
    'stopbits': serial.STOPBITS_ONE,
    'timeout': 10
}
