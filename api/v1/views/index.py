#!/usr/bin/python3
"""Index model holds the endpoint (route)"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


app = Flask(__name__)


@app_views.route('/status')
def status():
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each objects by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
