from bottle import route, default_app

from samples import features
from samples import sections


def index(**route_args):
    return 'Hello World!'


for s in sections:
    for f in features:
        route('/%s/%s' % (s, f))(index)

for f in features:
    route('/<locale:re:(en|ru)>/%s' % f)(index)

for f in features:
    route('/<user>/<repo>/%s' % f)(index)


main = default_app()
