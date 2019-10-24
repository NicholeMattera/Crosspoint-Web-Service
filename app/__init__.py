#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2019 Nichole Mattera
#

from flask import Flask
from app.routes import api_v1_bp

app = Flask(__name__)
app.register_blueprint(api_v1_bp, url_prefix='/api/v1')