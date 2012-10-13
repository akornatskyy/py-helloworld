from django.conf.urls import patterns, include, url

from samples import features
from samples import sections

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('helloworld.views',
    url("^welcome$", 'welcome'),
    url("^(?P<user>\w+)$", 'user_view'),
    url("^(?P<user>\w+)/(?P<repo>\w+)$", 'repo_view', name='repo')
)
urlpatterns += patterns('helloworld.views', *[
    url("^%s/%s$" % (s, f), 'welcome', name='%s-%s' % (s, f))
        for s in sections for f in features
])
urlpatterns += patterns('helloworld.views', *[
    url("^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, 'welcome', name=f)
        for f in features
])
