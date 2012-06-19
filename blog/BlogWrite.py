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

@view_config(name='post', request_method='GET')
def writePost(request):
    return render_to_response('templates/post.pt', {}, 
                              request=request)

@view_config(name='post', request_method='POST')
def savePost(request):
    p = Post(request.POST['text'], datetime.datetime.now())
    post.save(p)
    return Response("posted! " + p.text + " at date " + p.date)