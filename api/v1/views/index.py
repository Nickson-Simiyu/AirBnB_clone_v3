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
    stats = {}
    stats['amenities'] = storage.count('Amenity')
    stats['cities'] = storage.count('City')
    stats['places'] = storage.count('Place')
    stats['reviews'] = storage.count('Review')
    stats['states'] = storage.count('State')
    stats['users'] = storage.count('User')
    return jsonify(stats)
