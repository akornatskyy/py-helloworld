from django.conf.urls import include, url

from samples import features
from samples import sections

from .views import welcome, repo_view, user_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r"^welcome$", welcome),
    url(r"^(?P<user>\w+)$", user_view),
    url(r"^(?P<user>\w+)/(?P<repo>\w+)$", repo_view, name='repo')
]

urlpatterns += [
    url("^%s/%s$" % (s, f), welcome, name='%s-%s' % (s, f))
    for s in sections for f in features
]

urlpatterns += [
    url(r"^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, welcome, name=f)
    for f in features
]
