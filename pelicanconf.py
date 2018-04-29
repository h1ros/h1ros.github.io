#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import logging
try:
	AUTHOR = 'h1r03'
	SITENAME = "Data Science Blog"
	SITEURL = 'https://h1r03.github.io'

	PATH = 'content'

	TIMEZONE = 'America/Los_Angeles'

	DEFAULT_LANG = 'en'

	# Feed generation is usually not desired when developing
	FEED_ALL_ATOM = None
	CATEGORY_FEED_ATOM = None
	TRANSLATION_FEED_ATOM = None
	AUTHOR_FEED_ATOM = None
	AUTHOR_FEED_RSS = None
	#
	# Blogroll
	LINKS = (('Pelican', 'https://getpelican.com/'),
	         ('Python.org', 'https://python.org/'),
	         ('Jinja2', 'https://jinja.pocoo.org/'),
	         )

	# Social widget
	SOCIAL = (('twitter', 'https://twitter.com/__h1r0__'),
	          ('github', 'https://github.com/h1r03'),)
				

	          
	DEFAULT_PAGINATION = 10

	# Uncomment following line if you want document-relative URLs when developing
	#RELATIVE_URLS = True

	MARKUP = ('md', 'ipynb')

	PLUGIN_PATHS = ['pelican-plugins']
	PLUGINS = ['pelican-ipynb.markup']


	NOTEBOOK_DIR = 'notebooks'
	CODE_DIR = 'notebooks'
	STATIC_PATHS = ['md']


	# Theme
	THEME = "themes/pelican-clean-blog"


	IGNORE_FILES = ['.#*', '.ipynb_checkpoints']


	TYPOGRIFY = False

	# Pelican Clean Blog 
	HEADER_COVER = 'images/book-store-page-bookstore.jpg'


	# Ace Editor plugin
	MARKDOWN = {
	    'markdown.extensions.codehilite': {
	        'css_class': 'highlight',
	        'linenums': False,
	        'use_pygments': False
	    }
	}
except Exception as e:
	logging.exception('Exception was caught in pelicanconf.py')