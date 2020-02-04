#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2020 Nichole Mattera
#

from app.routes import api_v1_bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(api_v1_bp, url_prefix='/api/v1')