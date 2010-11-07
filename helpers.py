# coding: utf-8

from google.appengine.ext.webapp import template

def render(name, params=dict()):
    layout = 'layout'

    if not 'page' in params: 
        params['page'] = name
    if 'layout' in params:
        layout = params['layout']

    page = template.render('templates/%s.html' % name, params)
    params.update(dict(content=page))

    return template.render('templates/%s.html' % layout, params)
