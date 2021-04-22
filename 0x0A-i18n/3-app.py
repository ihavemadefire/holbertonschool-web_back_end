#!/usr/bin/env python3
'''This module is the main flask application'''
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''this is the config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello_world():
    '''The only route'''
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    '''This gets the locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    """ Main Function """
    app.run()
