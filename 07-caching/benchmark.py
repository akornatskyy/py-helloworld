
"""
"""

import os
import sys

try:
    import cProfile as profile
except ImportError:
    import profile

from pstats import Stats
from timeit import timeit

from samples import environ


path = os.getcwd()

frameworks = ['wheezy.web']
frameworks += ['django', 'flask']
frameworks = sorted(frameworks)


def start_response(status, headers):
    return None


def run(name, wrapper, number=100000):
    sys.path[0] = '.'
    print("\n%-11s   msec    rps  tcalls  funcs" % name)
    for framework in frameworks:
        os.chdir(os.path.join(path, framework))
        try:
            main = __import__('app', None, None, ['main']).main
            f = lambda: wrapper(main)
            time = timeit(f, number=number)
            st = Stats(profile.Profile().runctx('f()', globals(), locals()))
            print("%-11s %6.0f %6.0f %7d %6d" % (framework, 1000 * time,
                  number / time, st.total_calls, len(st.stats)))
            if 0:
                st = Stats(profile.Profile().runctx(
                    'timeit(f, number=number)', globals(), locals()))
                st.strip_dirs().sort_stats('time').print_stats(10)
            del sys.modules['app']
        except ImportError:
            print("%-15s not installed" % framework)


def build_wrapper(path_info):
    def wrapper(main):
        e = environ.copy()
        e['PATH_INFO'] = e['REQUEST_URI'] = path_info
        list(main(e, start_response))
    return wrapper


def run_batch(name):
    print('\n%s' % name)
    run('welcome', build_wrapper('/welcome'))
    run('memory', build_wrapper('/memory'))
    run('pylibmc', build_wrapper('/pylibmc'))
    run('memcache', build_wrapper('/memcache'))


if __name__ == '__main__':
    run_batch('no gzip')
    environ['HTTP_ACCEPT_ENCODING'] = 'gzip,deflate,sdch'
    run_batch('gzip')
