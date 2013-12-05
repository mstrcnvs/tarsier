# encoding: utf-8

from flask import current_app, render_template


@current_app.route('/list/')
def list():
	files = find_media()
	return render_template('media/list.html', files=files)


@current_app.route('/watch/<hash>/')
def watch(hash):
	files = find_media()
	return files[hash]
