#!/usr/bin/env python
# coding: utf-8

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

from tarsier import __title__, __version__

setup(
	name=__title__,
	version=__version__,
	license='GPLv3',
	url='https://github.com/mstrcnvs/tarsier/',
	packages=['tarsier'],
	scripts=['bin/tarsier'],
	install_requires=[
		'Flask==0.10.1',
		'python-magic==0.4.6'
	]
)
