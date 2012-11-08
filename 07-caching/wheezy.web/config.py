
from datetime import timedelta

from wheezy.core.pooling import EagerPool
from wheezy.caching import CacheClient
from wheezy.caching import MemoryCache
from wheezy.caching.memcache import MemcachedClient
from wheezy.caching.pylibmc import client_factory as pylibmc_factory
from wheezy.caching.pylibmc import MemcachedClient as PylibmcClient
from wheezy.http import CacheProfile


# cache config

memory_cache = MemoryCache()

memcache_cache = MemcachedClient(['unix:/tmp/memcached.sock'],
                                 key_encode=lambda key: key.replace(' ', '_'))

pylibmc_pool = EagerPool(lambda: pylibmc_factory(['/tmp/memcached.sock']),
                         size=100)

cache = CacheClient({
    'memory': memory_cache,
    'memcache': memcache_cache,
    'pylibmc':  PylibmcClient(pylibmc_pool)
}, default_namespace='memory')

# cache profiles

memory_profile = CacheProfile(
    'server', namespace='memory', duration=timedelta(minutes=15),
    vary_environ=['HTTP_ACCEPT_ENCODING'])
pylibmc_profile = CacheProfile(
    'server', namespace='pylibmc', duration=timedelta(minutes=15),
    vary_environ=['HTTP_ACCEPT_ENCODING'])
memcache_profile = CacheProfile(
    'server', namespace='memcache', duration=timedelta(minutes=15),
    vary_environ=['HTTP_ACCEPT_ENCODING'])
