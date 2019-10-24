#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2019 Nichole Mattera
#

def infoRequest():
    return b'I'

def getTie(output: int):
    return bytearray(f'{output}%', 'ascii')

def createTie(input: int, output: int):
    return bytearray(f'{input}*{output}!', 'ascii')
