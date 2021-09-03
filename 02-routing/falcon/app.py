import falcon

from samples import features
from samples import sections


class Welcome(object):

    def on_get(self, req, resp, **route_args):
        resp.status = falcon.HTTP_200
        resp.text = ('Hello World!')


main = falcon.App(media_type='text/plain')

for s in sections:
    for f in features:
        main.add_route('/%s/%s' % (s, f), Welcome())

for f in features:
    main.add_route('/{locale}/%s' % f, Welcome())

for f in features:
    main.add_route('/{locale}/{repo}/%s' % f, Welcome())
