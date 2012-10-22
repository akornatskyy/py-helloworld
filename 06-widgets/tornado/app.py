
"""
"""

import uimodules

from tornado.template import Loader
from tornado.util import ObjectDict


def main(name):
    loader = Loader(root_directory=name)
    template = loader.load('welcome.html')
    modules = {'_modules': ObjectDict([
        ('greeting', uimodules.Greeting(loader)),
        ('greetings', uimodules.Greetings(loader))
    ])}
    return lambda ctx: template.generate(**dict(ctx, **modules))
