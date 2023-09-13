from django.urls import include, re_path

from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    re_path(r'^welcome$', views.welcome, name='welcome'),
    re_path(r'^memory$', views.memory, name='memory'),
    re_path(r'^pylibmc$', views.pylibmc, name='pylibmc'),
    re_path(r'^memcache$', views.memcache, name='memcache'),
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^helloworld/', include('helloworld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
