#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2019 Nichole Mattera
#

import json
from flask import Response

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
        # Example: `V12X08 A12X08`
        if (len(message) == 15):
            video=message[1:6]
            audio=message[8:13]

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
        # Example: `Out03 In01 All`
        if message.startswith(b'Out'):
            self.input = int(message[9:11])
            self.output = int(message[3:5])
        # Example: `In05 All`
        elif message.startswith(b'In'):
            self.input = int(message[2:4])
            self.output = 0
        # Example: `12`
        elif len(input) == 4:
            self.input = int(input)
            self.output = output
        else:
            self.input = 0
            self.output = 0