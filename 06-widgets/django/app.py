
"""
"""

import sys


def main(name):
    # unload django modules, if any, so we can reconfigure settings
    modules = [m for m in sys.modules.keys() if m.startswith('dj')]
    for m in modules:
        del sys.modules[m]

    import django
    from django.conf import settings
    from django.template import Context
    from django.template import loader

    settings.configure(
        DEBUG = True,
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [name],
                'OPTIONS': {
                    'builtins': ['djangotags'],
                }
            },
        ]
    )
    django.setup()
    template = loader.get_template('welcome.html')
    return lambda ctx: template.render(ctx)
