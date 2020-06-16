from django.conf.urls import include, url

from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^memory$', views.memory, name='memory'),
    url(r'^pylibmc$', views.pylibmc, name='pylibmc'),
    url(r'^memcache$', views.memcache, name='memcache'),
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^helloworld/', include('helloworld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
