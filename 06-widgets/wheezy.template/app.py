
"""
"""

from wheezy.html.utils import escape_html as escape
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader


def main(name):
    searchpath = [name]
    engine = Engine(
        loader=FileLoader(searchpath),
        extensions=[
            CoreExtension()
        ]
    )
    engine.compiler.source_lineno = 0;
    engine.global_vars.update({'h': escape})

    template = engine.get_template('welcome.html')
    return template.render
