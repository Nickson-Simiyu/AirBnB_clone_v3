#!/usr/bin/python3
"""creates the Blueprint for flask application"""
from flask import Blueprint
# Create a Blueprint instance with url prefix '/api/v1'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
# Import everything in the package api.v1.views.index
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
