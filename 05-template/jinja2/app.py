
"""
"""

from jinja2 import Environment
from jinja2 import FileSystemLoader


def main(name):
    searchpath=[name]
    env = Environment(
        loader=FileSystemLoader(searchpath),
        extensions=[]
    )
    template = env.get_template('welcome.html')
    return template.render
