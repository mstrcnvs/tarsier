# encoding: utf-8

import os
import magic
import hashlib


class MediaFile(object):
	def __init__(self, root, name):
		self.root = root
		self.name = name
		self.full_path = os.path.join(root, name)
		self.hash = hashlib.sha1(self.full_path.encode('utf-8')).hexdigest()[:8]

	@property
	def size(self):
		return os.path.getsize(self.full_path)

	@property
	def mimetype(self):
		return magic.from_file(self.full_path, mime=True)
