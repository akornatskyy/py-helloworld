from pyramid.config import Configurator
from pyramid.response import Response

from samples import features
from samples import names
from samples import repos
from samples import sections


def welcome(request):
    for name in names:
        request.route_path(name)
    return Response('Hello World!')


def user(request):
    user = request.matchdict['user']
    for name in repos:
        request.route_path('repo', user=user, repo=name)
    return Response('Hello World!')


def repo(request):
    for name in features:
        request.route_path(name, **request.matchdict)
    return Response('Hello World!')


config = Configurator()

config.add_route('welcome', '/welcome')
config.add_view(welcome, route_name='welcome')

config.add_route('user', '/{user}')
config.add_view(user, route_name='user')

config.add_route('repo', '/{user}/{repo}')
config.add_view(repo, route_name='repo')

for s in sections:
    for f in features:
        route_name = '%s-%s' % (s, f)
        config.add_route(route_name, '/%s/%s' % (s, f))
        config.add_view(welcome, route_name=route_name)

for f in features:
    config.add_route(f, '/{user}/{repo}/%s' % f)
    config.add_view(welcome, route_name=f)

main = config.make_wsgi_app()
