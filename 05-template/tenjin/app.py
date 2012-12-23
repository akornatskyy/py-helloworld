
"""
"""

import sys

if sys.version_info[0] >= 3:
    str_type = str
else:
    str_type = unicode

import tenjin
from tenjin.helpers import capture_as, captured_as, cache_as
tenjin.set_template_encoding('UTF-8')
try:
    from webext import escape_html as escape
except ImportError:
    from tenjin.helpers import escape


def main(name):
    engine = tenjin.Engine(
        path=[name],
        postfix='.html',
        cache=tenjin.MemoryCacheStorage(),
        pp=None)
    helpers = {
        'to_str': str_type,
        'escape': escape,
        'capture_as': capture_as,
        'captured_as': captured_as,
        'cache_as': cache_as
    }
    return lambda ctx: engine.render('welcome.html', ctx, helpers)
