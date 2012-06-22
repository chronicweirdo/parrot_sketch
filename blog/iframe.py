'''
Created on Jun 19, 2012

@author: silviu
'''
from blog.entity import post
from blog.entity.post import Post
from pyramid.renderers import render_to_response
from pyramid.response import Response
from pyramid.view import view_config
import datetime

@view_config(name='iframe', request_method='GET')
def serveIframe(request):
    return render_to_response('templates/iframe.pt', {}, 
                              request=request)