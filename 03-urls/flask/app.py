from flask import Flask
from flask import url_for

from samples import features
from samples import names
from samples import repos
from samples import sections


main = Flask(__name__)


@main.route('/welcome')
def welcome():
    for name in names:
        url_for(name)
    return 'Hello World!'


@main.route('/<user>')
def show_user(user):
    for name in repos:
        url_for('repo', user=user, repo=name)
    return 'Hello World!'


@main.route('/<user>/<repo>', endpoint='repo')
def show_repo(user, repo):
    for name in features:
        url_for(name, user=user, repo=repo)
    return 'Hello World!'


for s in sections:
    for f in features:
        main.route('/%s/%s' % (s, f), endpoint='%s-%s' % (s, f))(welcome)

for f in features:
    main.route('/<user>/<repo>/%s' % f, endpoint=f)(welcome)
