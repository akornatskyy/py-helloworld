import warnings

from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory

from samples import features
from samples import sections


class WelcomeHandler(BaseHandler):

    def get(self):
        response = HTTPResponse()
        response.write('Hello World!')
        return response

seo_urls = [(f, WelcomeHandler) for f in features]
dynamic_urls = [(f, WelcomeHandler) for f in features]

all_urls = []
all_urls += [url('%s/%s' % (s, f), WelcomeHandler)
             for s in sections for f in features]
all_urls += [url('{locale:(en|ru)}/', seo_urls)]
all_urls += [url('{user}/{repo}/', dynamic_urls)]

warnings.simplefilter('ignore')
main = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options={}
)
