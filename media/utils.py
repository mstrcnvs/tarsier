# encoding: utf-8

import os
from hashlib import sha1

from flask import current_app, abort


class MediaFile(object):
	def __init__(self, root, name):
		self.root = root
		self.name = name
		self.full_path = os.path.join(root, name)
		self.hash = sha1(self.full_path.encode('utf-8')).hexdigest()[:8]
		self.size = os.path.getsize(self.full_path)

		_, ext = os.path.splitext(name)
		if ext == '.ogg':
			self.mimetype = 'video/ogg'
		elif ext == '.mp4':
			self.mimetype = 'video/mp4'


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
