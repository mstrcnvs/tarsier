# encoding: utf-8

import os
from hashlib import sha1

from flask import current_app


def find_media():
	folder = current_app.config['MEDIA_FOLDER'].decode('utf-8')
	return [
		MediaFile(root, file)
		for root, dirs, files in os.walk(folder)
		for file in files
		if os.path.splitext(file)[-1] in ['.avi', '.mp4']
	]


class MediaFile(object):
	def __init__(self, root, name):
		self.root = root
		self.name = name
		self.full_path = os.path.join(root, name)
		self.hash = sha1(self.full_path.encode('utf-8')).hexdigest()[:8]
