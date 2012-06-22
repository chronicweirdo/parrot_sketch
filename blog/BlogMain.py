'''
Created on Jun 19, 2012

@author: silviu
'''
from blog.entity.post import loadFirst
from pyramid.configuration import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response
from pyramid.static import static_view
from pyramid.view import view_config
from wsgiref.simple_server import make_server

@view_config()
def home(request):
    p = loadFirst()
    return render_to_response('templates/home.pt', 
                              {'project':'blog', 'text': p.text},
                              request=request)

if __name__ == '__main__':
    config = Configurator()
    config.scan('blog')
    config.add_static_view('img', 'blog:img');
    config.add_static_view('document', 'blog:documents');
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()