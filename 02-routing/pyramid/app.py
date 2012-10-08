from pyramid.config import Configurator
from pyramid.response import Response

from samples import features
from samples import sections


def welcome(request):
    return Response('Hello World!')


config = Configurator()

for s in sections:
    for f in features:
        route_name = 'static-%s-%s' % (s, f)
        config.add_route(route_name, '/%s/%s' % (s, f))
        config.add_view(welcome, route_name=route_name)

for f in features:
    route_name = 'seo-%s' % f
    config.add_route(route_name, '/{locale:(en|ru)}/%s' % f)
    config.add_view(welcome, route_name=route_name)

for f in features:
    route_name = 'dynamic-%s' % f
    config.add_route(route_name, '/{user}/{repo}/%s' % f)
    config.add_view(welcome, route_name=route_name)

main = config.make_wsgi_app()
