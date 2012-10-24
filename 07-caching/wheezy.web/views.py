
import config

from wheezy.core.comp import ntob
from wheezy.http import HTTPResponse
from wheezy.http.transforms import gzip_transform
from wheezy.web import handler_cache
from wheezy.web.handlers import BaseHandler
from wheezy.web.transforms import handler_transforms


hello = ntob(''.join(['%s. Hello World! ' % i for i in xrange(500)]),
             'utf8')


class WelcomeHandler(BaseHandler):

    @handler_transforms(gzip_transform(compress_level=6))
    def get(self):
        response = HTTPResponse()
        response.write_bytes(hello)
        return response


class MemoryHandler(BaseHandler):

    @handler_cache(config.memory_profile)
    @handler_transforms(gzip_transform(compress_level=6))
    def get(self):
        response = HTTPResponse()
        response.write_bytes(hello)
        return response


class PylibmcHandler(BaseHandler):

    @handler_cache(config.pylibmc_profile)
    @handler_transforms(gzip_transform(compress_level=6))
    def get(self):
        response = HTTPResponse()
        response.write_bytes(hello)
        return response


class MemcacheHandler(BaseHandler):

    @handler_cache(config.memcache_profile)
    @handler_transforms(gzip_transform(compress_level=6))
    def get(self):
        response = HTTPResponse()
        response.write_bytes(hello)
        return response
