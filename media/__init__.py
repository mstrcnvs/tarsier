# encoding: utf-8

from __future__ import absolute_import

from flask import Blueprint, render_template, abort
from media.utils import find_media

media = Blueprint('media', __name__, template_folder='templates')


@media.route('/list/')
def list():
	files = find_media()
	return render_template('media/list.html', files=files)


@media.route('/watch/<hash>/')
def watch(hash):
	files = find_media()

	try:
		media = filter(lambda f: f.hash == hash, files)
		media = media[0]
	except IndexError:
		abort(404)

	return render_template('media/watch.html', media=media)


@media.route('/stream/<hash>/')
def stream(hash):
	files = find_media()

	try:
		media = filter(lambda f: f.hash == hash, files)
		media = media[0]
	except IndexError:
		abort(404)

	return ''
