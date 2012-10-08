from django.conf.urls import patterns, include, url

from samples import features
from samples import sections

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('helloworld.views', *[
    url("^%s/%s$" % (s, f), 'welcome')
        for s in sections for f in features
])
urlpatterns += patterns('helloworld.views', *[
    url("^(?P<locale>en|ru)/%s$" % f, 'welcome')
        for s in sections for f in features
])
urlpatterns += patterns('helloworld.views', *[
    url("^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, 'welcome')
        for f in features
])
