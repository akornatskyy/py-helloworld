
import views

from wheezy.routing import url


all_urls = [
    url('welcome', views.WelcomeHandler),
    url('memory', views.MemoryHandler),
    url('pylibmc', views.PylibmcHandler),
    url('memcache', views.MemcacheHandler),
]
