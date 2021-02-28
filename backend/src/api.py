import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from flasgger import Swagger

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)
# access http://localhost:5000/apidocs to show generated documentation by swagger
Swagger(app)

#db_drop_and_create_all()

## ROUTES
# Main page endpoint for public 
@app.route('/drinks', methods=['GET'])
def get_drinks():
    
    #swagger documentation for drinks endpoint
    """
    This is coffee shop drinks API
    Call this api return the drinks in the audacity coffee shop
    ---
    tags:
      - coffee shop full stack API
    parameters:
      - name: drinks
        in: path
        type: list
        required: true
        description: drinks in the coffee shop
      - name: success
        in: query
        type: boolean
        description: success flag
    responses:
      200:
        description: drinks in the coffee shop
        schema:
          id: drink
          properties:
            title:
              type: string
              description: the drink name
              default:""
            recipe:
              type: array
              description: list of drink's parts
              items:
                type: object
                additionalProperties:
                    type: string
              default: [{"color": "#ffffff", "name": "", "parts": 1}]
    """
    
    drinks = Drink.query.all()
    short_form_drinks = [drink.short() for drink in drinks]
    
    return jsonify({
        'success': True,
        'drinks': short_form_drinks
    }), 200

# Main page endpoint for barista and managers
@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    drinks = Drink.query.all()
    drinks_details = [drink.long() for drink in drinks]

    return jsonify({
        'success': True,
        'drinks': drinks_details
    }), 200


# Adding new drink
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drink(payload):
    drink_details = request.get_json()
    print(drink_details)

    try:
        new_drink = Drink()
        new_drink.title = drink_details['title']
        recipe = drink_details['recipe']
        new_drink.recipe = recipe if type(recipe) == str else json.dumps(recipe)
        new_drink.insert()

    except Exception:
        abort(400)

    return jsonify({
        'success': True, 
        'drinks': [new_drink.long()]
    })


# Edit on existing drink
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drink(payload, id):
    edited_data = request.get_json()
    selected_drink = Drink.query.filter(Drink.id == id).one_or_none()
    print(edited_data)

    if not selected_drink:
        abort(404)

    try:
        selected_drink.title = edited_data['title']
        recipe = edited_data['recipe']
        selected_drink.recipe = recipe if type(recipe) == str else json.dumps(recipe) 
        selected_drink.update()
        
    except Exception:
        abort(400)

    return jsonify({
        'success': True,
        'drinks': [selected_drink.long()]
    }), 200


# Delete a drink
@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    deleted_drink = Drink.query.filter(Drink.id == id).one_or_none()

    if not deleted_drink:
        abort(404)

    try:
        deleted_drink.delete()
        
    except Exception:
        abort(400)

    return jsonify({'success': True, 'delete': id}), 200

## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(AuthError)
def auth_error(error):
    print(error)
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code

@app.errorhandler(400)
def bad_request(error):
    print(error)
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400



