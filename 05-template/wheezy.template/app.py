
"""
"""

from wheezy.template.engine import Engine
from wheezy.template.loader import FileLoader
from wheezy.template.ext.core import CoreExtension


def main(name):
    searchpath=[name]
    engine = Engine(
        loader=FileLoader(searchpath),
        extensions=[
            CoreExtension()
        ]
    )

    template = engine.get_template('welcome.html')
    return template.render
