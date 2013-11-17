import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render
from samples import features
from samples import names
from samples import repos


log = logging.getLogger(__name__)


class WelcomeController(BaseController):

    def index(self):
        for name in names:
            url(name)
        return 'Hello World!'

    def user(self, user):
        for name in repos:
            url('repo', user=user, repo=name)
        return 'Hello World!'

    def repo(self, user, repo):
        for name in features:
            url(name, user=user, repo=repo)
        return 'Hello World!'
