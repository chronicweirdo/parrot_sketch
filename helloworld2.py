from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

def hello_world(request):
   return Response('Hello %(name)s!' % request.matchdict)

#@view_config(route_name='ok', request_method='POST', permission='read')
#@view_config(route_name='fred')
#@view_config()
@view_config(name='fred', request_method='GET')
def fred_view(request):
    return Response('fred')

if __name__ == '__main__':
   config = Configurator()
   config.add_route('hello', '/hello/{name}')
   config.add_view(hello_world, route_name='hello')
   config.scan()
   app = config.make_wsgi_app()
   server = make_server('0.0.0.0', 8088, app)
   server.serve_forever()
