from django.http import HttpResponse, HttpResponseNotFound


def welcome(request, **route_args):
    return HttpResponse("Hello World!")


def error404(request, exception):
    return HttpResponseNotFound()
