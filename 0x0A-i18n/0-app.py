#!/usr/bin/env python3
'''This module is the main flask application'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    '''The only route'''
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
