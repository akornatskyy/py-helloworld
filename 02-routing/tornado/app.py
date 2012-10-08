import tornado.web
import tornado.wsgi

from samples import features
from samples import sections


class WelcomeHandler(tornado.web.RequestHandler):

    def get(self, **route_args):
        self.write("Hello World!")


urls = [
    ("/%s/%s" % (s, f), WelcomeHandler)
        for s in sections for f in features
]
urls += [
    ("/(?P<locale>en|ru)/%s" % f, WelcomeHandler)
        for f in features
]
urls += [
    ("/(?P<user>\w+)/(?P<repo>\w+)/%s" % f, WelcomeHandler)
        for f in features
]

main = tornado.wsgi.WSGIApplication(urls)
