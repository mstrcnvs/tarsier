# encoding: utf-8

import json
import os
import shutil
import time

from tarsier import __title__
from tarsier.media.file import MediaFile
from tarsier.media.utils import get_appdir


def get_webfiles():
	path = get_appdir(__title__)

	if not os.path.exists(path):
		os.makedirs(path)

	try:
		with open(os.path.join(path, 'webfiles.json'), 'r+') as f:
			return json.loads(f.read() or '{}')
	except IOError:
		return {}


def update_webfile(hash, name, timestamp=None):
	path = get_appdir(__title__)

	if not os.path.exists(path):
		os.makedirs(path)

	data = get_webfiles()

	if not timestamp:
		timestamp = int(time.time())

	data[os.path.join(hash, name)] = timestamp

	try:
		with open(os.path.join(path, 'webfiles.json'), 'w+') as f:
			f.write(json.dumps(data))

		return True
	except IOError:
		return False


def remove_webfile(hash, name):
	path = get_appdir(__title__)
	data = get_webfiles()

	try:
		os.remove(os.path.join(path, 'webfiles', hash, name))

		if len(os.listdir(os.path.join(path, 'webfiles', hash))) == 0:
			os.rmdir(os.path.join(path, 'webfiles', hash))

		del data[os.path.join(hash, name)]
	except IOError:
		pass

	try:
		with open(os.path.join(path, 'webfiles.json'), 'w+') as f:
			f.write(json.dumps(data))

		return True
	except IOError:
		return False


def clean_webfiles(maxage=0):
	path = get_appdir(__title__)
	data = get_webfiles()

	for name, timestamp in data.items():
		if int(time.time()) > timestamp + maxage:
			try:
				hash, name = os.path.split(name)
				os.remove(os.path.join(path, 'webfiles', hash, name))

				if len(os.listdir(os.path.join(path, 'webfiles', hash))) == 0:
					os.rmdir(os.path.join(path, 'webfiles', hash))

				del data[os.path.join(hash, name)]
			except IOError:
				pass

	try:
		with open(os.path.join(path, 'webfiles.json'), 'w+') as f:
			f.write(json.dumps(data))

		return True
	except IOError:
		return False


class WebMediaFile(MediaFile):
	extension = '.webmedia'

	def __init__(self, origin):
		self.origin = origin

		root = os.path.join(get_appdir(__title__), 'webfiles', origin.hash)
		name = origin.hash + '.' + self.extension.strip('. ')

		super(WebMediaFile, self).__init__(root, name)

		if not self.exists():
			self.create()

		update_webfile(origin.hash, name)

	def exists(self):
		return os.path.exists(self.full_path)

	def create(self):
		if not os.path.exists(self.root):
			os.makedirs(self.root)

		self.convert()

	def convert(self):
		shutil.copyfile(self.origin.full_path, self.full_path)
