# encoding: utf-8

from flask import Flask

# Blueprints
from media import media

tarsier = Flask(__name__)
tarsier.register_blueprint(media)
