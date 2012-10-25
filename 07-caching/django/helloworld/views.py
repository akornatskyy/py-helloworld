
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.gzip import gzip_page


hello = ''.join(['%s. Hello World! ' % i for i in xrange(500)])


@gzip_page
def welcome(request):
    return HttpResponse(hello)


@cache_page(60 * 15, cache="memory")
@gzip_page
def memory(request):
    return HttpResponse(hello)


@cache_page(60 * 15, cache="pylibmc")
@gzip_page
def pylibmc(request):
    return HttpResponse(hello)


@cache_page(60 * 15, cache="memcache")
@gzip_page
def memcache(request):
    return HttpResponse(hello)
