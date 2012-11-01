
from datetime import timedelta

from wheezy.caching import CacheClient
from wheezy.caching import MemoryCache
from wheezy.caching.memcache import client_factory as memcache_factory
from wheezy.caching.pools import EagerPool
from wheezy.caching.pools import Pooled
from wheezy.caching.pylibmc import client_factory as pylibmc_factory
from wheezy.http import CacheProfile


# cache config

memory_cache = MemoryCache()

memcache_cache = memcache_factory(['unix:/tmp/memcached.sock'],
        key_encode=lambda key: key.replace(' ', '_'))

pylibmc_pool = EagerPool(lambda: pylibmc_factory(['/tmp/memcached.sock']),
                         size=100)

cache = CacheClient({
    'memory': lambda: memory_cache,
    'memcache': lambda: memcache_cache,
    'pylibmc': lambda: Pooled(pylibmc_pool)
}, default_namespace='memory')

cache_factory = lambda: cache

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
