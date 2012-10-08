from flask import Flask

from samples import features
from samples import sections


main = Flask(__name__)


def welcome(**route_args):
    return 'Hello World!'


for s in sections:
    for f in features:
        main.route('/%s/%s' % (s, f))(welcome)

for f in features:
    main.route('/<locale>/%s' % f)(welcome)

for f in features:
    main.route('/<user>/<repo>/%s' % f)(welcome)
