
import config


from wheezy.http import HTTPResponse
from wheezy.http.transforms import gzip_transform
from wheezy.web import handler_cache
from wheezy.web.handlers import BaseHandler
from wheezy.web.transforms import handler_transforms


hello = ''.join(['%s. Hello World! ' % i for i in range(500)]).encode('utf8')


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


if config.pylibmc_profile:
    class PylibmcHandler(BaseHandler):

        @handler_cache(config.pylibmc_profile)
        @handler_transforms(gzip_transform(compress_level=6))
        def get(self):
            response = HTTPResponse()
            response.write_bytes(hello)
            return response
else:
    class PylibmcHandler(BaseHandler):
        def get(self):
            raise ImportError()


class MemcacheHandler(BaseHandler):

    @handler_cache(config.memcache_profile)
    @handler_transforms(gzip_transform(compress_level=6))
    def get(self):
        response = HTTPResponse()
        response.write_bytes(hello)
        return response
