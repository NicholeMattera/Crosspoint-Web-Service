#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2019 Nichole Mattera
#

from app import api_v1_bp
from app.models.responses import ErrorResponse, InfoResponse, TieResponse
from app.models.serial_requests import infoRequest, getTie, createTie
from flask import request
import serial

def connect():
    return serial.Serial(
        '/dev/ttyUSB0',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=10
    )

@api_v1_bp.route('/info', methods=['GET'])
def get_info():
    try:
        s = connect()
        s.write(infoRequest())
        return InfoResponse(s.readline()).response(200)
    except serial.serialutil.SerialException as e:
        return ErrorResponse(0, 'Device not available.').response(500)

@api_v1_bp.route('/tie/<int:output>', methods=['GET'])
def get_tie(output):
    if output < 1 or output > 8:
        return ErrorResponse(4, 'Output field is out of range.').response(500)
    
    try:
        s = connect()
        s.write(getTie(output))
        return TieResponse(s.readline(), output).response(200)
    except serial.serialutil.SerialException as e:
        return ErrorResponse(0, 'Device not available.').response(500)

@api_v1_bp.route('/tie', methods=['POST'])
def post_tie():
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
        s = connect()
        s.write(createTie(data['input'], data['output']))
        return TieResponse(s.readline()).response(200)
    except serial.serialutil.SerialException as e:
        return Error(0, 'Device not available.').response(500)


@api_v1_bp.route('/tie/<int:index>', methods=['DELETE'])
def delete_tie():
    if output < 1 or output > 8:
        return Error(4, 'Output field is out of range.').response(500)

    try:
        s = connect()
        s.write(createTie(0, data['output']))
        return TieResponse(s.readline())
    except serial.serialutil.SerialException as e:
        return Error(0, 'Device not available.').response(500)
