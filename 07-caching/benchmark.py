import cProfile as profile
import os
import sys
from pstats import Stats
from timeit import repeat, timeit

from samples import environ

path = os.path.join(os.getcwd(), os.path.dirname(__file__))

frameworks = ["wheezy.web"]
frameworks += ["django", "flask"]
frameworks = sorted(frameworks)


def start_response(status, headers):
    assert status == "200 OK"
    return None


def run(name, wrapper, number=2000):
    path = os.path.dirname(__file__)
    print("\n%-11s   msec      rps  tcalls  funcs" % name, flush=True)
    for framework in frameworks:
        sys.path[0] = os.path.join(path, framework)
        os.chdir(os.path.join(path, framework))
        try:
            if name == "pylibmc":
                import pylibmc
            main = __import__("app", None, None, ["main"]).main
            f = lambda: wrapper(main)
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
            print("%-15s not installed" % framework, flush=True)


def build_wrapper(path_info):
    def wrapper(main):
        e = environ.copy()
        e["PATH_INFO"] = e["REQUEST_URI"] = path_info
        list(main(e, start_response))

    return wrapper


def run_batch(name):
    print("\n%s" % name, flush=True)
    run("welcome", build_wrapper("/welcome"))
    run("memory", build_wrapper("/memory"))
    run("pylibmc", build_wrapper("/pylibmc"))
    run("memcache", build_wrapper("/memcache"))


if __name__ == "__main__":
    run_batch("no gzip")
    environ["HTTP_ACCEPT_ENCODING"] = "gzip,deflate,sdch"
    run_batch("gzip")
