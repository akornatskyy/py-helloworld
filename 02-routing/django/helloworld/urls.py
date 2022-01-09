from django.urls import include, re_path

from samples import features
from samples import sections

from .views import welcome

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


handler404 = 'helloworld.views.error404'


urlpatterns = [
    re_path("^%s/%s$" % (s, f), welcome)
    for s in sections for f in features
]

urlpatterns += [
    re_path(r"^(?P<locale>en|ru)/%s$" % f, welcome)
    for f in features
]

urlpatterns += [
    re_path(r"^(?P<user>\w+)/(?P<repo>\w+)/%s$" % f, welcome)
    for f in features
]
