import cProfile as profile
import gc
import importlib
import os
import sys
from io import BytesIO
from pstats import Stats
from timeit import repeat, timeit

environ = {
    "HTTP_ACCEPT": "text/html,application/xhtml+xml,application/xml;"
    "q=0.9,*/*;q=0.8",
    "HTTP_ACCEPT_CHARSET": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "HTTP_ACCEPT_ENCODING": "gzip,deflate,sdch",
    "HTTP_ACCEPT_LANGUAGE": "uk,en-US;q=0.8,en;q=0.6",
    "HTTP_CACHE_CONTROL": "max-age=0",
    "HTTP_CONNECTION": "keep-alive",
    "HTTP_HOST": "127.0.0.1:8080",
    "HTTP_USER_AGENT": "Mozilla/5.0 (X11; Linux i686)",
    "PATH_INFO": "/welcome",
    "QUERY_STRING": "",
    "REMOTE_ADDR": "127.0.0.1",
    "REQUEST_METHOD": "GET",
    "REQUEST_URI": "/welcome",
    "SCRIPT_NAME": "",
    "SERVER_NAME": "localhost",
    "SERVER_PORT": "8080",
    "SERVER_PROTOCOL": "HTTP/1.1",
    "uwsgi.node": "localhost",
    "uwsgi.version": "1.2.6",
    "wsgi.errors": None,
    "wsgi.file_wrapper": None,
    "wsgi.input": BytesIO(b""),
    "wsgi.multiprocess": False,
    "wsgi.multithread": False,
    "wsgi.run_once": False,
    "wsgi.url_scheme": "http",
    "wsgi.version": (1, 0),
}

frameworks = ["bottle", "falcon", "pyramid", "wheezy.web", "wsgi"]
# slow
frameworks += ["bobo", "django", "flask", "cherrypy"]
# very slow
# frameworks += ["cherrypy"]
frameworks = sorted(frameworks)


def start_response(status, headers, exec_info=None):
    assert status == "200 OK"
    return None


def run(number=10000):
    path = os.path.dirname(__file__)
    print("              msec      rps  tcalls  funcs", flush=True)
    for framework in frameworks:
        sys.path[0] = os.path.join(path, framework)
        try:
            main = __import__("app", None, None, ["main"]).main
            f = lambda: list(main(environ.copy(), start_response))
            # time = timeit(f, number=number)
            time = min(repeat(f, number=number))
            st = Stats(profile.Profile().runctx("f()", globals(), locals()))
            print(
                "%-11s %6.0f %8.0f %7d %6d"
                % (
                    framework,
                    1000 * time,
                    number / time,
                    st.total_calls,
                    len(st.stats),
                ),
                flush=True
            )
            if 0:
                st = Stats(
                    profile.Profile().runctx(
                        "timeit(f, number=number)", globals(), locals()
                    )
                )
                st.strip_dirs().sort_stats("time").print_stats(10)
            del sys.modules["app"]
        except ImportError:
            print("%-20s not installed" % framework, flush=True)
        modules = [m for m in sys.modules.keys() if m.endswith("helloworld")]
        for m in modules:
            del sys.modules[m]


if __name__ == "__main__":
    run()
