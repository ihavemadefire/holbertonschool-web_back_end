#!/usr/bin/env python3
'''This module is the main flask application'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import UnknownTimeZoneError, timezone
app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    '''this is the config class.'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    '''The only route'''
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    '''This gets the locale'''
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    if g.user:
        user_pref = g.user.get('locale')
        if user_pref and user_pref in Config.LANGUAGES:
            return user_pref
    req_head = request.accept_languages.best_match(app.config['LANGUAGES'])
    if req_head:
        return req_head
    return Config.BABEL_DEFAULT_LOCALE


def get_user(user_id):
    '''returns user object'''
    return users.get(user_id)


@app.before_request
def before_request():
    '''this function rens before other functions'''
    user_id = request.args.get("login_as")
    if user_id:
        user_id = int(user_id)
    g.user = get_user(user_id)


@babel.timezoneselector
def get_timezone():
    '''This gets the timezone'''
    tz = request.args.get('timezone')
    if tz:
        try:
            timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass
    if g.user:
        user_tz = g.user.get('timezone')
        if user_tz:
            try:
                timezone(user_tz)
                return user_tz
            except UnknownTimeZoneError:
                pass
    return Config.BABEL_DEFAULT_TIMEZONE


if __name__ == "__main__":
    """ Main Function """
    app.run()
