
import os
from datetime import timedelta

from wheezy.core.pooling import EagerPool
from wheezy.caching import CacheClient
from wheezy.caching import MemoryCache
from wheezy.caching.memcache import MemcachedClient
from wheezy.http import CacheProfile


# cache config

memory_cache = MemoryCache()

memcached_host = os.environ.get('MEMCACHED_HOST', '127.0.0.1')


memcache_cache = MemcachedClient([memcached_host],
                                 key_encode=lambda key: key.replace(' ', '_'))


cache = CacheClient({
    'memory': memory_cache,
    'memcache': memcache_cache
}, default_namespace='memory')

# cache profiles

memory_profile = CacheProfile(
    'server', namespace='memory', duration=timedelta(minutes=15),
    vary_environ=['HTTP_ACCEPT_ENCODING'])

memcache_profile = CacheProfile(
    'server', namespace='memcache', duration=timedelta(minutes=15),
    vary_environ=['HTTP_ACCEPT_ENCODING'])

try:
    import pylibmc
    from wheezy.caching.pylibmc import client_factory as pylibmc_factory
    from wheezy.caching.pylibmc import MemcachedClient as PylibmcClient
except ImportError:
    pylibmc_profile = None
else:
    pylibmc_pool = EagerPool(lambda: pylibmc_factory([memcached_host]),
                         size=100)
    cache.namespaces['pylibmc'] =  PylibmcClient(pylibmc_pool)
    pylibmc_profile = CacheProfile(
        'server', namespace='pylibmc', duration=timedelta(minutes=15),
        vary_environ=['HTTP_ACCEPT_ENCODING'])
