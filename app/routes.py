#
# This file is part of CrosspointWebService. https://github.com/NicholeMattera/CrosspointWebService
# Copyright (C) 2020 Nichole Mattera
#

from flask import Blueprint
from app.views.info_view import InfoView
from app.views.tie_view import TieView, TieIDView

api_v1_bp = Blueprint('api_v1', __name__)
api_v1_bp.add_url_rule('/info', view_func=InfoView.as_view('info_view'))
api_v1_bp.add_url_rule('/tie', view_func=TieView.as_view('tie_view'))
api_v1_bp.add_url_rule('/tie/<int:output>', view_func=TieIDView.as_view('tie_id_view'))
