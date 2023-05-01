#!/usr/bin/python3
"""Creates a new view for Amenity objects that handles all default RESTFul API actions"""
from flask import Flask, request, abort, jsonify
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = Amenity().all()
    amenities_list = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenities_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieves a Amenity object"""
    amenity = Amenity().get(amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Deletes a Amenity object"""
    amenity = Amenity().get(amenity_id)
    if not amenity:
        abort(404)
    amenity.delete()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    """Creates a Amenity"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    amenity = Amenity(**request.get_json())
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Updates a Amenity"""
    amenity = Amenity().get(amenity_id)
    if not amenity:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
