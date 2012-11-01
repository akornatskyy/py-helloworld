from memcache import Client as MemcacheClient
from pylibmc import Client as PylibmcClient
from werkzeug.contrib.cache import MemcachedCache as MemcachedBase

from flask import Flask
from flask.ext.cache import Cache


# cache backends

class MemcacheCache(MemcachedBase):

    def import_preferred_memcache_lib(self, servers):
        return MemcacheClient(servers)


class PylibmcCache(MemcachedBase):

    def import_preferred_memcache_lib(self, servers):
        return PylibmcClient(servers)


def memcache(app, config, args, kwargs):
    args.append(config['CACHE_MEMCACHED_SERVERS'])
    return MemcacheCache(*args, **kwargs)


def pylibmc(app, config, args, kwargs):
    args.append(config['CACHE_MEMCACHED_SERVERS'])
    return PylibmcCache(*args, **kwargs)


# config

main = Flask(__name__)

memory_cache = Cache(main, with_jinja2_ext=False, config={
    'CACHE_TYPE': 'simple'
})


pylibmc_cache = Cache(main, with_jinja2_ext=False, config={
    'CACHE_TYPE': 'app.pylibmc',
    'CACHE_MEMCACHED_SERVERS': ('/tmp/memcached.sock',)
})


memcache_cache = Cache(main, with_jinja2_ext=False, config={
    'CACHE_TYPE': 'app.memcache',
    'CACHE_MEMCACHED_SERVERS': ('unix:/tmp/memcached.sock',)
})


hello = ''.join(['%s. Hello World! ' % i for i in xrange(500)])


# views

@main.route('/welcome')
def welcome():
    return hello


@main.route('/memory')
@memory_cache.cached(timeout=60 * 15)
def memory():
    return hello


@main.route('/pylibmc')
@pylibmc_cache.cached(timeout=60 * 15)
def pylibmc_view():
    return hello


@main.route('/memcache')
@memcache_cache.cached(timeout=60 * 15)
def memcache_view():
    return hello
