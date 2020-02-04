#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2020 Nichole Mattera
#

from flask import Response
import json

class JSONSerializableResponse:
    def jsonEncode(self):
        return json.dumps(self.__dict__)

    def response(self, status: int):
        return Response(
            self.jsonEncode(),
            status=status,
            mimetype='application/json'
        )

class ErrorResponse(JSONSerializableResponse):
    def __init__(self, num: int, message: str):
        self.num = num
        self.message = message

class InfoResponse(JSONSerializableResponse):
    def __init__(self, message: bytes):
        msg_str = message.decode('ascii')

        # Example: `V12X08 A12X08`
        if (len(msg_str) == 15):
            video=msg_str[1:6]
            audio=msg_str[8:13]

            self.video_inputs = int(video[0:2])
            self.video_outputs = int(video[3:5])
            self.audio_inputs = int(audio[0:2])
            self.audio_outputs = int(audio[3:5])
        else:
            self.video_inputs = 0
            self.video_outputs = 0
            self.audio_inputs = 0
            self.audio_outputs = 0

class TieResponse(JSONSerializableResponse):
    def __init__(self, message: bytes, output: int = 0):
        msg_str = message.decode('ascii')

        # Example: `Out03 In01 All`
        if msg_str.startswith('Out'):
            self.input = int(msg_str[9:11])
            self.output = int(msg_str[3:5])
        # Example: `In05 All`
        elif msg_str.startswith('In'):
            self.input = int(msg_str[2:4])
            self.output = 0
        # Example: `12`
        elif len(msg_str) == 4:
            self.input = int(msg_str)
            self.output = output
        else:
            self.input = 0
            self.output = 0