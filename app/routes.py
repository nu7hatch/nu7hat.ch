# coding: utf-8

from itty import *
from app.helpers import * 

@get('/')
def index(request):
    face = open('misc/face').read()
    return render('index', dict(face=face))
    
@get('/blog')
def blog(request):
    return render('blog')
    
@get('/blog/:slug')
def blog_entry(request):
    pass
    
@get('/(?P<filename>.+)')
def simple_media(request, filename):
    return serve_static_file(request, filename, root="static")
