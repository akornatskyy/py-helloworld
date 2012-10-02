
"""
"""

import profile
import sys

from pstats import Stats
from timeit import timeit


if sys.version_info[0] >= 3:
    b = b''
else:
    b = ''

environ = {
        'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
                       'q=0.9,*/*;q=0.8',
        'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch',
        'HTTP_ACCEPT_LANGUAGE': 'uk,en-US;q=0.8,en;q=0.6',
        'HTTP_CACHE_CONTROL': 'max-age=0',
        'HTTP_CONNECTION': 'keep-alive',
        'HTTP_HOST': 'vm0.dev.local:8080',
        'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux i686)',
        'PATH_INFO': '/welcome',
        'QUERY_STRING': '',
        'REMOTE_ADDR': '127.0.0.1',
        'REQUEST_METHOD': 'GET',
        'REQUEST_URI': '/welcome',
        'SCRIPT_NAME': '',
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': '8080',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'uwsgi.node': 'localhost',
        'uwsgi.version': '1.2.6',
        'wsgi.errors': None,
        'wsgi.file_wrapper': None,
        'wsgi.input': None,
        'wsgi.multiprocess': False,
        'wsgi.multithread': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'http',
        'wsgi.version': (1, 0),
}


def start_response(status, headers):
    return None


def run(number=100000):
    print("             ttime  tcalls  funcs")
    for framework in ['bobo', 'bottle', 'cherrypy', 'flask', 'pyramid',
                      'tornado', 'wheezy.web', 'wsgi']:
        sys.path[0] = framework
        try:
            main = __import__('app', None, None, ['main']).main
            def wrapper():
                b.join(main(environ.copy(), start_response))
            time = timeit(wrapper, number=number)
            st = Stats(profile.Profile().runctx(
                'wrapper()', globals(), locals()))
            print("%-10s %7.3f %7d %6d" % (framework, time,
                st.total_calls, len(st.stats)))
            del sys.modules['app']
        except ImportError:
            print("%-15s not installed" % framework)


if __name__ == '__main__':
    run()
