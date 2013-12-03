# encoding: utf-8
from flask import Blueprint

media = Blueprint('media', __name__)


@media.route('/list/')
def media_list():
	return ''


@media.route('/watch/')
def media_watch():
	return ''
