import tornado.web
import tornado.wsgi

from tornado.web import URLSpec

from samples import features
from samples import names
from samples import repos
from samples import sections


class WelcomeHandler(tornado.web.RequestHandler):

    def get(self):
        for name in names:
            self.reverse_url(name)
        self.write("Hello World!")


class UserHandler(tornado.web.RequestHandler):

    def get(self, user):
        for name in repos:
            self.reverse_url('repo', user, name)
        self.write("Hello World!")


class RepoHandler(tornado.web.RequestHandler):

    def get(self, user, repo):
        for name in features:
            self.reverse_url(name, user, repo)
        self.write("Hello World!")


urls = [
    ("/welcome", WelcomeHandler),
    ("/(?P<user>\w+)", UserHandler),
    URLSpec("/(?P<user>\w+)/(?P<repo>\w+)", RepoHandler, name="repo")
]
urls += [
    URLSpec("/%s/%s" % (s, f), WelcomeHandler, name="%s-%s" % (s, f))
    for s in sections for f in features
]
urls += [
    URLSpec("/(?P<user>\w+)/(?P<repo>\w+)/%s" % f, WelcomeHandler, name=f)
    for f in features
]

main = tornado.wsgi.WSGIApplication(urls)
