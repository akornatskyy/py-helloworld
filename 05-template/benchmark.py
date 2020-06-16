
"""
"""

import os
import sys

try:
    import cProfile as profile
except ImportError:
    import profile

from pstats import Stats
from timeit import timeit, repeat

from samples import items
from samples import user


path = os.path.join(os.getcwd(), os.path.dirname( __file__))

frameworks = ['django', 'jinja2', 'tornado', 'wheezy.template']
frameworks += ['mako']
frameworks = sorted(frameworks)


def run(name, ctx, number=10000):
    sys.path[0] = '.'
    print("\n%-16s   msec      rps  tcalls  funcs" % name)
    for framework in frameworks:
        os.chdir(os.path.join(path, framework))
        if not os.path.exists(name):
            print("%-22s not available" % framework)
            continue
        try:
            main = __import__('app', None, None, ['main']).main
            render = main(name)
            f = lambda: render(ctx)
            # time = timeit(f, number=number)
            time = min(repeat(f, number=number))
            st = Stats(profile.Profile().runctx('f()', globals(), locals()))
            print("%-16s %6.0f %8.0f %7d %6d" % (framework, 1000 * time,
                  number / time, st.total_calls, len(st.stats)))
            if 0:
                st = Stats(profile.Profile().runctx(
                    'timeit(f, number=number)', globals(), locals()))
                st.strip_dirs().sort_stats('time').print_stats(10)
            del sys.modules['app']
        except ImportError:
            print("%-22s not installed" % framework)


def run_batch(ctx):
    print("\nlen(items) == %s" % len(ctx['items']))
    run('01-initial', ctx)
    run('02-include', ctx)
    run('03-extends', ctx)
    run('04-preprocess', ctx)


if __name__ == '__main__':
    run_batch({'user': user, 'items': []})
    run_batch({'user': user, 'items': items})
