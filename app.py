#!/usr/bin/env python
# encoding: utf-8

from tarsier import tarsier

tarsier.config.update(
	MEDIA_FOLDER=''
)

if __name__ == '__main__':
	# Run a development server
	tarsier.run(debug=True)
