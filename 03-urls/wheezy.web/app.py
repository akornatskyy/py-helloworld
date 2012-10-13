import warnings

from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory

from samples import features
from samples import names
from samples import repos
from samples import sections


class WelcomeHandler(BaseHandler):

    def get(self):
        for name in names:
            self.path_for(name)
        response = HTTPResponse()
        response.write('Hello World!')
        return response


class UserHandler(BaseHandler):

    def get(self):
        for name in repos:
            self.path_for('repo', repo=name)
        response = HTTPResponse()
        response.write('Hello World!')
        return response


class RepoHandler(BaseHandler):

    def get(self):
        for name in features:
            self.path_for(name)
        response = HTTPResponse()
        response.write('Hello World!')
        return response


dynamic_urls = [url(f, WelcomeHandler, name=f) for f in features]

all_urls = []
all_urls += [
        url('welcome', WelcomeHandler),
        url('{user}', UserHandler),
        url('{user}/{repo}', RepoHandler, name='repo'),
]
all_urls += [url('%s/%s' % (s, f), WelcomeHandler, name='%s-%s' % (s, f))
        for s in sections for f in features]
all_urls += [url('{user}/{repo}/', dynamic_urls)]

warnings.simplefilter('ignore')
main = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options={}
)
