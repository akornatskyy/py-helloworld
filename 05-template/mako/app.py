
"""
"""

from mako.lookup import TemplateLookup


def main(name):
    directories=[name]
    template_lookup = TemplateLookup(
        directories=directories
    )
    template = template_lookup.get_template('welcome.html')
    return lambda ctx: template.render(**ctx)
