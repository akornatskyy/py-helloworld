import warnings

from wheezy.http import WSGIApplication
from wheezy.http.middleware import http_cache_middleware_factory
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory

from config import cache_factory
from urls import all_urls


options = {}

# HTTPCacheMiddleware
options.update({
    'http_cache_factory': cache_factory
})

warnings.simplefilter('ignore')
main = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        http_cache_middleware_factory,
        path_routing_middleware_factory
    ],
    options=options
)
