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

@view_config(route_name='imageiframe', request_method='GET')
def imageIframe(request):
    return render_to_response('templates/imageiframe.pt',
                              {'image': request.matchdict['image']},
                              request=request)

@view_config(name='iframe', request_method='GET')
def serveIframe(request):
    # 'document/iframe2.html'
    return render_to_response('templates/iframe.pt',
                              {'iframe': 'imageiframe/au.png'}, 
                              request=request)