import os
import sys

from samples import features
from samples import sections


conf_dir = os.path.dirname(os.path.abspath(__file__))
conf_dir = os.path.join(conf_dir, 'helloworld')
sys.path.insert(0, conf_dir)
from helloworld.config.middleware import make_app
main = make_app({}, full_stack=False, static_files=False, cache_dir='')
routes_map = main.config['routes.map']
routes_map.connect('welcome', '/{controller}', action='index')
routes_map.connect('user', '/{user}', controller='welcome', action='user')
routes_map.connect('repo', '/{user}/{repo}',
                   controller='welcome', action='repo')

for s in sections:
    for f in features:
        route_name = '%s-%s' % (s, f)
        routes_map.connect(route_name, '/%s/%s' % (s, f),
                           controller='welcome', action='index')

for f in features:
    routes_map.connect(f, '/{user}/{repo}/%s' % f,
                       controller='welcome', action='index')
