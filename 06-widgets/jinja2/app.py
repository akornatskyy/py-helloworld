
"""
"""

from jinja2 import Environment
from jinja2 import FileSystemLoader


def main(name):
    env = Environment(
        loader=FileSystemLoader(searchpath=[name]),
        extensions=[]
    )
    template = env.get_template('welcome.html')
    return template.render
