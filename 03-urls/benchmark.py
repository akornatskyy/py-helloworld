
"""
"""

import os
import profile
import sys

from pstats import Stats
from timeit import timeit

from samples import environ


if sys.version_info[0] >= 3:
    b = b''
else:
    b = ''

path = os.getcwd()

frameworks = ['pyramid', 'wheezy.web']
frameworks = sorted(frameworks)


def start_response(status, headers):
    return None


def run(name, wrapper, number=10000):
    sys.path[0] = '.'
    print("\n%-11s   msec    rps  tcalls  funcs" % name)
    for framework in frameworks:
        os.chdir(os.path.join(path, framework))
        try:
            main = __import__('app', None, None, ['main']).main
            wrapper(main)
            time = timeit(lambda: wrapper(main), number=number)
            st = Stats(profile.Profile().runctx(
                'wrapper(main)', globals(), locals()))
            print("%-11s %6.0f %6.0f %7d %6d" % (framework, 1000 * time,
                number / time, st.total_calls, len(st.stats)))
            del sys.modules['app']
        except ImportError:
            print("%-15s not installed" % framework)


def build_wrapper(path_info):
    def wrapper(main):
        e = environ.copy()
        e['PATH_INFO'] = e['REQUEST_URI'] = path_info
        b.join(main(e, start_response))
    return wrapper


if __name__ == '__main__':
    run('static', build_wrapper('/welcome'))
    run('merge', build_wrapper('/jsmith'))
    run('route', build_wrapper('/jsmith/repo1'))
