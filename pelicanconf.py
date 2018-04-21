#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/__h1r0__'),
          ('github', 'https://github.com/h1r03'),)
			

          
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins', ]
PLUGINS = ['ipynb.markup']

NOTEBOOK_DIR = 'notebooks'
CODE_DIR = 'notebooks'
STATIC_PATHS = ['md']

# Theme
THEME = "simple"


IGNORE_FILES = ['.#*', '.ipynb_checkpoints']


TYPOGRIFY = False