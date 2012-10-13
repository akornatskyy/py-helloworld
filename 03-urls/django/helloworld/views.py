from django.http import HttpResponse
from django.core.urlresolvers import reverse

from samples import features
from samples import names
from samples import repos


def welcome(request):
    for name in names:
        reverse(name)
    return HttpResponse("Hello World!")


def user_view(request, user):
    for name in repos:
        reverse('repo', kwargs={'user': user, 'repo': name})
    return HttpResponse("Hello World!")


def repo_view(request, user, repo):
    for name in features:
        reverse(name, kwargs={'user': user, 'repo': repo})
    return HttpResponse("Hello World!")
