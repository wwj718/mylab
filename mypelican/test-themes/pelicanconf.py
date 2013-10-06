#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'wuwenjie'
SITENAME = u'writing for time'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'zh'
#THEME = "bootstrap2"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('my github', 'https://github.com/wwj718'),
          ('my gmail', 'wuwenjie718@gmail.com'),
	     ('我的豆瓣', 'http://www.douban.com/people/59672556/'),)

# Social widget
'''
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
'''
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#wwj test 2013-8-9
THEME = "themes/wwjbootstrap2"
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh': '%Y-%m-%d',
}

DISQUS_SITENAME = u"wwj718"