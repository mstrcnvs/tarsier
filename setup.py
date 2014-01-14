#!/usr/bin/env python
# coding: utf-8

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

from tarsier import __version__

setup(
	name='tarsier',
	version=__version__,
	license='GPLv3',
	url='https://github.com/mstrcnvs/tarsier/',
	packages=['tarsier'],
	scripts=['bin/tarsier'],
	install_requires=[
		'Flask==0.10.1',
	]
)
