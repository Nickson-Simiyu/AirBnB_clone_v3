#!/usr/bin/python3
"""Index model holds the endpoint (route)"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each objects by type"""
    models_available = {"User": "users",
                        "Amenity": "amenities", "City": "cities",
                        "Place": "places", "Review": "reviews",
                        "State": "states"}
    stats = {}
    for cls in models_available.keys():
        stats[models_available[cls]] = storage.count(cls)
    return jsonify(stats)
