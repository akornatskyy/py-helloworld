from circuits.web import Controller
from circuits.web.wsgi import Application


class Root(Controller):

    def welcome(self):
        return "Hello World!"


main = Application() + Root()
