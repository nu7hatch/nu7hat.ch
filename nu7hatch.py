# coding: utf-8

import sys
import os

sys.path = ['lib/itty'] + sys.path

from itty import get, run_itty
from google.appengine.ext.webapp import template


analytics = open('misc/analytics').read()

def render(name, params={}):
    return template.render('templates/%s.html' % name, params)


@get('/')
def index(request):
    face = open('misc/face').read()
    return render('index', {'face': face, 'analytics': analytics})
    
@get('/blog')
def blog(request):
    pass
    
@get('/blog/:slug')
def blog_entry(request):
    pass
    
    
def main():
    run_itty('appengine')

if __name__ == '__main__':
    main()
