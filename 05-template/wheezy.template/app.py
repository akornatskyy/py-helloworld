
"""
"""

from wheezy.template.engine import Engine
from wheezy.template.loader import FileLoader
from wheezy.template.ext.core import CoreExtension


def main(name):
    searchpath = [name]
    engine = Engine(
        loader=FileLoader(searchpath),
        extensions=[
            CoreExtension(token_start='#')
        ]
    )
    engine = Engine(
        loader=PreprocessLoader(engine),
        extensions=[
            CoreExtension()
        ]
    )

    template = engine.get_template('welcome.html')
    return template.render


class PreprocessLoader(object):

    def __init__(self, engine, ctx=None):
        self.engine = engine
        self.ctx = ctx or {}

    def load(self, name):
        return self.engine.render(name, self.ctx, {}, {})
