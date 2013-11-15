
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

frameworks = ['bottle', 'falcon', 'pyramid', 'wheezy.web']
frameworks += ['django', 'flask', 'tornado']
#frameworks = ['web2py']
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


if __name__ == '__main__':
    run('static[0]', build_wrapper('/section0/feature0'))
    run('static[-1]', build_wrapper('/section9/feature19'))
    run('dynamic[0]', build_wrapper('/jsmith/dotfiles/feature0'))
    run('dynamic[-1]', build_wrapper('/jsmith/dotfiles/feature19'))
    run('seo[0]', build_wrapper('/en/feature0'))
    run('seo[-1]', build_wrapper('/ru/feature9'))
    run('missing', build_wrapper('/not-found'))
