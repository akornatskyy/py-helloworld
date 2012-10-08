
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

frameworks = ['pyramid', 'tornado', 'wheezy.web']

def start_response(status, headers):
    return None


def run(name, wrapper, number=1000):
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
    run('static[0]', build_wrapper('/section0/feature0'))
    run('static[-1]', build_wrapper('/section9/feature19'))
    run('dynamic[0]', build_wrapper('/jsmith/dotfiles/feature0'))
    run('dynamic[-1]', build_wrapper('/jsmith/dotfiles/feature19'))
    run('seo[0]', build_wrapper('/en/feature0'))
    run('seo[-1]', build_wrapper('/ru/feature9'))
    run('missing', build_wrapper('/not-found'))
