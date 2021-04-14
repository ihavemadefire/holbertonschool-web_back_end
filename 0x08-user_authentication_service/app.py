#!/usr/bin/env python3
'''This module contains the main application'''
from flask import Flask, jsonify, request, abort
from auth import Auth
from flask.helpers import make_response
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''basic route'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''user route'''
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        if AUTH.register_user(email, password):
            return jsonify({"email": email,
                            "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    '''login session route'''
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session = AUTH.create_session(email)
        r = make_response(jsonify({"email": email, "message": "logged in"}))
        r.set_cookie("session_id", session)
        return session
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
