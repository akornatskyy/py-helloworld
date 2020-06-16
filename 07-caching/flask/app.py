import os
import logging

from memcache import Client as MemcacheClient

from flask import Flask
from flask_caching import Cache
from flask.logging import default_handler

# config

main = Flask(__name__)


def handle_exception(e):
    raise e

main.handle_exception = handle_exception

memory_cache = Cache(config={'CACHE_TYPE': 'simple'})
memory_cache.init_app(main)

memcached_host = os.environ.get('MEMCACHED_HOST', '127.0.0.1')

try:
    from pylibmc import Client as PylibmcClient

    pylibmc_cache = Cache(config={
        'CACHE_TYPE': 'memcached',
        'CACHE_MEMCACHED_SERVERS': PylibmcClient([memcached_host])
    })
    pylibmc_cache.init_app(main)
except ImportError:
    pylibmc_cache = None


memcache_cache = Cache(config={
    'CACHE_TYPE': 'memcached',
    'CACHE_MEMCACHED_SERVERS': MemcacheClient([memcached_host])
})
memcache_cache.init_app(main)

hello = ''.join(['%s. Hello World! ' % i for i in range(500)])


# views

@main.route('/welcome')
def welcome():
    return hello


@main.route('/memory')
@memory_cache.cached(timeout=60 * 15)
def memory():
    return hello


if pylibmc_cache:
    @main.route('/pylibmc')
    @pylibmc_cache.cached(timeout=60 * 15)
    def pylibmc_view():
        return hello
else:
    @main.route('/pylibmc')
    def pylibmc_view():
        raise ImportError()


@main.route('/memcache')
@memcache_cache.cached(timeout=60 * 15)
def memcache_view():
    return hello
