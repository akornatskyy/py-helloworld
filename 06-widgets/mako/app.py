
"""
"""

from mako.lookup import TemplateLookup


def main(name):
    template_lookup = TemplateLookup(
        directories=[name]
    )
    template = template_lookup.get_template('welcome.html')
    return lambda ctx: template.render(**ctx)
