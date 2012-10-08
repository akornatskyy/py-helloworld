from django.http import HttpResponse


def welcome(request, **route_args):
    return HttpResponse("Hello World!")
