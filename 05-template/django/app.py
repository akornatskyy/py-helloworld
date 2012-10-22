
"""
"""

import sys


def main(name):
    # unload django modules, if any, so we can reconfigure settings
    modules = [m for m in sys.modules.keys() if m.startswith('dj')]
    for m in modules:
        del sys.modules[m]

    from django.conf import settings
    from django.template import Context
    from django.template import loader

    settings.configure(
        TEMPLATE_DIRS=[name],
        TEMPLATE_LOADERS=(
            ('django.template.loaders.cached.Loader', (
                'django.template.loaders.filesystem.Loader',
            )),
        )
    )
    template = loader.get_template('welcome.html')
    return lambda ctx: template.render(Context(ctx))
