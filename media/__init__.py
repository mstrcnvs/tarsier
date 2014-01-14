# encoding: utf-8

from __future__ import absolute_import

import re

from flask import Blueprint, Response, request, render_template
from media.utils import find_media, find_media_or_404

media = Blueprint('media', __name__, template_folder='templates')


@media.route('/')
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

	stream = False
	initial = 0
	final = media.size - 1

	if 'Range' in request.headers:
		stream = True

		ranges = re.findall(r'\d+', request.headers['Range'])
		initial = int(ranges[0])

		if len(ranges) > 1:
			final = int(ranges[1])

	with open(media.full_path, 'rb') as file:
		if stream:
			file.seek(initial)

		data = file.read(final - initial)

	response = Response(
		data,
		status='200',
		headers={
			'Content-Type': media.mimetype,
			'Content-Length': str(final - initial),
			'Content-Transfer-Encoding': 'binary',
			'Accept-Ranges': 'bytes',
		},
		mimetype=media.mimetype
	)

	if stream:
		response.status = '206'
		response.headers['Content-Range'] = '%s-%s/%s' % (
			initial,
			final,
			final - initial
		)

	return response
