# encoding: utf-8

from __future__ import absolute_import

from flask import Blueprint, render_template
from media.utils import find_media, find_media_or_404

media = Blueprint('media', __name__, template_folder='templates')


@media.route('/list/')
def list():
	files = find_media()
	return render_template('media/list.html', files=files)


@media.route('/watch/<hash>/')
def watch(hash):
	media = find_media_or_404(hash=hash)

	return render_template('media/watch.html', media=media)


@media.route('/stream/<hash>/')
def stream(hash):
	media = find_media_or_404(hash=hash)

	return ''
