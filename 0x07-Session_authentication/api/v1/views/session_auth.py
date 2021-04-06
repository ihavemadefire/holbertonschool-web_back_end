#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask.helpers import make_response
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """ POST /api/v1/auth_session/login
    Return:
      - jsonified user
    """
    # get user info
    email = request.form.get("email")
    password = request.form.get("password")
    # validate user info
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    # find user
    list = User.search({"email": email})
    # validate
    if len(list) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = list[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    # build response
    session_id = auth.create_session(user.id)
    cookie = getenv("SESSION_NAME")
    response = make_response(user.to_json())
    response.set_cookie(cookie, session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    '''Def destroy session'''
    from api.v1.app import auth
    logout = auth.destroy_session(request)
    if logout is False:
        return abort(404)
    return jsonify({}), 200
