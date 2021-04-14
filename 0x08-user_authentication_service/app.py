#!/usr/bin/env python3
'''This module contains the main application'''
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from flask.helpers import make_response
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''basic index route'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''user creation route'''
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        if AUTH.register_user(email, password):
            return jsonify({"email": email,
                            "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''login session route'''
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session = AUTH.create_session(email)
        r = make_response(
            jsonify({"email": email, "message": "logged in"}))
        r.set_cookie("session_id", session)
        return r
    else:
        return abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    '''User logout function'''
    s_id = request.cookies.get('session_id')
    if s_id:
        u = AUTH.get_user_from_session_id(s_id)
        if u:
            AUTH.destroy_session(u.id)
            return redirect("/")
    return abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    '''Fetch User profile function function'''
    s_id = request.cookies.get('session_id')
    if s_id:
        u = AUTH.get_user_from_session_id(s_id)
        if u:
            return jsonify({"email": u.email})
    return abort(403)


@app.route('/reset_password', methods=['GET'], strict_slashes=False)
def get_reset_password_token():
    '''Fetch User profile function function'''
    email = request.form.get("email")
    try:
        u = AUTH._db.find_user_by(email=email)
        if u:
            token = AUTH._db.get_reset_password_token(email)
            return jsonify({{"email": email, "reset_token": token}}), 200
    except NoResultFound
        return abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
