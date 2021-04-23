#!/usr/bin/env python3
'''This module is the main flask application'''
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''this is the config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    '''returns user object'''
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get("login_as")
    if user_id:
        g.user = get_user(int(user_id))


@app.route('/')
def hello_world():
    '''The only route'''
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    '''This gets the locale'''
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    """ Main Function """
    app.run()
