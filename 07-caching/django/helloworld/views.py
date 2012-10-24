
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

hello = 'Hello World!' * 350


def welcome(request):
    return HttpResponse(hello)


@cache_page(60 * 15, cache="memory")
def memory(request):
    return HttpResponse(hello)


@cache_page(60 * 15, cache="pylibmc")
def pylibmc(request):
    return HttpResponse(hello)


@cache_page(60 * 15, cache="memcache")
def memcache(request):
    return HttpResponse(hello)
