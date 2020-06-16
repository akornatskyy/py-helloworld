from django.conf.urls import include, url

from samples import features
from samples import sections

from .views import welcome

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


handler404 = 'helloworld.views.error404'


urlpatterns = [
    url("^%s/%s$" % (s, f), welcome)
    for s in sections for f in features
]

urlpatterns += [
    url(r"^(?P<locale>en|ru)/%s$" % f, welcome)
    for f in features
]

urlpatterns += [
    url(r"^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, welcome)
    for f in features
]
