#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2019 Nichole Mattera
#

from flask import Flask, Blueprint

app = Flask(__name__)

api_v1_bp = Blueprint('api_v1', __name__)
from app import routes
app.register_blueprint(api_v1_bp, url_prefix='/api/v1')