from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

@view_config(
    route_name='home',
    renderer='templates/home.jinja2')

@view_config( 
    route_name='away',
    renderer='templates/away.jinja2')

def home(request):
    return{'greet':'Welcome','name':'Home'}

def away(request):
    return{'greet':'Welcome','name':'Away'}
 

if __name__ == "__main__":
    with Configurator() as config:
        config.include("pyramid_jinja2")
        config.add_static_view(name='static',path='static')
        config.add_route('home','/welcome')
        config.add_route('away', '/away')
        config.scan() 
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()