import cProfile as profile
import os
import sys
from pstats import Stats
from timeit import repeat, timeit

from samples import environ

path = os.path.join(os.getcwd(), os.path.dirname(__file__))

frameworks = ["bottle", "falcon", "wheezy.web"]
frameworks += ["django", "flask", "pyramid"]
frameworks = sorted(frameworks)


def start_response(status, headers, exec_info=None):
    assert status.startswith('200') or status.startswith('404')
    return None


def run(name, wrapper, number=5000):
    path = os.path.dirname(__file__)
    print("\n%-11s   msec      rps  tcalls  funcs" % name, flush=True)
    for framework in frameworks:
        sys.path[0] = os.path.join(path, framework)
        try:
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
        modules = [m for m in sys.modules.keys() if m.endswith("helloworld")]
        for m in modules:
            del sys.modules[m]


def build_wrapper(path_info):
    def wrapper(main):
        e = environ.copy()
        e["PATH_INFO"] = e["REQUEST_URI"] = path_info
        list(main(e, start_response))

    return wrapper


if __name__ == "__main__":
    run("static[0]", build_wrapper("/section0/feature0"))
    run("static[-1]", build_wrapper("/section9/feature19"))
    run("dynamic[0]", build_wrapper("/jsmith/dotfiles/feature0"), 1000)
    run("dynamic[-1]", build_wrapper("/jsmith/dotfiles/feature19"), 1000)
    run("seo[0]", build_wrapper("/en/feature0"), 1000)
    run("seo[-1]", build_wrapper("/ru/feature9"), 1000)
    run("missing", build_wrapper("/not-found"), 1000)
