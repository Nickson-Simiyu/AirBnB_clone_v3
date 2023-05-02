#!/usr/bin/python3
"""endpoint (route) will be to return the status of your API"""
from flask import Flask
from api.v1.views import app_views
from models import storage
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(_name_)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_storage(exception):
    """ closes the session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


if _name_ == "_main_":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
