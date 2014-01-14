# encoding: utf-8

__version__ = '0.1'

from flask import Flask

from tarsier.media import media

tarsier = Flask(__name__)
tarsier.register_blueprint(media)
