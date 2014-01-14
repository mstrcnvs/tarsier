# encoding: utf-8

from __future__ import absolute_import

from flask import Flask

from tarsier.media import media

tarsier = Flask(__name__)
tarsier.register_blueprint(media)
