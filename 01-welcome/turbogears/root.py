from tg import expose
from helloworld.lib.base import BaseController


class RootController(BaseController):

    @expose()
    def welcome(self):
        return "Hello World!"
