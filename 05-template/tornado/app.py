
"""
"""

from tornado.template import Loader


def main(name):
    loader = Loader(root_directory=name)
    template = loader.load('welcome.html')
    return lambda ctx: template.generate(**ctx)
