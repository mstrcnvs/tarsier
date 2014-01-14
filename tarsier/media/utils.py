# encoding: utf-8

import os

from flask import current_app, abort

from tarsier.media.file import MediaFile


def find_media(hash=None):
	folder = current_app.config['MEDIA_FOLDER'].decode('utf-8')
	files = [
		MediaFile(root, file)
		for root, dirs, files in os.walk(folder)
		for file in files
		if os.path.splitext(file)[-1] in ['.ogg', '.mp4']
	]

	if hash:
		try:
			media = filter(lambda f: f.hash == hash, files)
			return media[0]
		except IndexError:
			return None
	else:
		return files


def find_media_or_404(hash):
	return find_media(hash=hash) or abort(404)
