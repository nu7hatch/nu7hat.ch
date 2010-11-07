# coding: utf-8

from itty import get
from helpers import * 

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
