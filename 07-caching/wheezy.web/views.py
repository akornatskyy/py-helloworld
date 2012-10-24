
import config

from wheezy.http import HTTPResponse
from wheezy.web import handler_cache
from wheezy.web.handlers import BaseHandler

hello = 'Hello World!' * 350


class WelcomeHandler(BaseHandler):

    def get(self):
        response = HTTPResponse()
        response.write(hello)
        return response


class MemoryHandler(BaseHandler):

    @handler_cache(config.memory_profile)
    def get(self):
        response = HTTPResponse()
        response.write(hello)
        return response


class PylibmcHandler(BaseHandler):

    @handler_cache(config.pylibmc_profile)
    def get(self):
        response = HTTPResponse()
        response.write(hello)
        return response


class MemcacheHandler(BaseHandler):

    @handler_cache(config.memcache_profile)
    def get(self):
        response = HTTPResponse()
        response.write(hello)
        return response
