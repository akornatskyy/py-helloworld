
"""
"""

from wheezy.html.utils import escape_html as escape
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader
from wheezy.template.loader import PreprocessLoader


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
    engine.global_vars.update({'h': escape})

    template = engine.get_template('welcome.html')
    return template.render
