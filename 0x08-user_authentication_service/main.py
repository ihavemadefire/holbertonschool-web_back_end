#!/usr/bin/env python3
"""
Main file
"""
from app import AUTH
import requests


def register_user(email: str, password: str) -> None:
    '''Instance of the register_user def for testing'''
    payload = {"email": email, "password": password}
    r = requests.post("http://localhost:5000/users", payload)
    print(r.status_code == 200)
    assert r.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    '''Instance of the def for testing'''
    payload = {"email": email, "password": password}
    r = requests.post("http://localhost:5000/sessions", payload)
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    '''Instance of the log_in def for testing'''
    payload = {"email": email, "password": password}
    r = requests.post("http://localhost:5000/sessions", payload)
    assert r.status_code == 200
    assert r.json() == {"email": email, "message": "logged in"}


def profile_unlogged() -> None:
    '''Instance of the profile_unlogged def for testing'''
    r = requests.get("http://localhost:5000/profile")
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    '''Instance of the profile_logged def for testing'''
    u = AUTH.get_user_from_session_id(session_id)
    cookie = {'session_id': session_id}
    r = requests.post("http://localhost:5000/profile", cookie)
    assert r.status_code == 200
    assert r.json() == {"email": u.email}


def log_out(session_id: str) -> None:
    '''Instance of the def for testing'''
    cookie = {'session_id': session_id}
    r = requests.post("http://localhost:5000/profile", cookie)
    assert r.status_code == 200
    assert r.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    '''Instance of the log_out def for testing'''
    payload = {'email': email}
    r = requests.post('http://localhost:5000/reset_password', payload)
    token = AUTH.find_user_by(email=email).reset_token
    assert r.status_code == 200
    assert r.json() == {"email": email, "reset_token": token}


def update_password(email: str, reset_token: str, new_password: str) -> None:
    '''Instance of the update_password def for testing'''
    p = {"email": email, "reset_token": reset_token,
         "new_password": new_password}
    r = requests.post('http://localhost:5000/reset_password', p)
    assert r.status_code == 200
    assert r.json() == ({"email": email, "message": "Password updated"})


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
