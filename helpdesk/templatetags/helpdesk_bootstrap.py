"""
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2013 Lubomir Gelo. All Rights Reserved. See LICENSE for details.

templatetags/helpdesk_boostrap.py - Bootstrap template helpers

"""

from django.template import Library
from django.conf import settings

BOOTSTRAP_DEFAULTS = {
    '_base_url': 	      '//netdna.bootstrapcdn.com/bootstrap/3.0.1',
    'jquery_url': 	      '//code.jquery.com/jquery.min.js',
    'fa_url':	          '//netdna.bootstrapcdn.com/font-awesome/4.0.1/css/font-awesome.css',
    'css_url':		      None,
    'js_url':             None,
    'theme_url':          '/static/helpdesk/helpdesk.css',
}

BOOTSTRAP = BOOTSTRAP_DEFAULTS.copy()
BOOTSTRAP.update(getattr(settings, 'BOOTSTRAP', {}))

register = Library()

@register.filter(name='class')
def add_class(field, classes):
	return field.as_widget(attrs={"class": classes})

@register.simple_tag
def fa_css():
    return '<link rel="stylesheet" media="screen" href="%s">' % BOOTSTRAP['fa_url']

@register.simple_tag
def bootstrap_css():
    return '<link rel="stylesheet" media="screen" href="%s">' % (BOOTSTRAP['css_url'] or ('%s/css/bootstrap.min.css' % BOOTSTRAP['_base_url']))

@register.simple_tag
def theme_css():
    return '<link rel="stylesheet" media="screen" href="%s">' % BOOTSTRAP['theme_url']


@register.simple_tag
def bootstrap_js(jquery=True):
	output = ''
	if jquery:
   		output += '<script src="%s"></script>' % BOOTSTRAP['jquery_url']
	output += '<script src="%s"></script>' % (BOOTSTRAP['js_url'] or ('%s/js/bootstrap.min.js' % BOOTSTRAP['_base_url']))
	
	return output