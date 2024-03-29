from io import BytesIO

environ = {
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
                   'q=0.9,*/*;q=0.8',
    'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch',
    'HTTP_ACCEPT_LANGUAGE': 'uk,en-US;q=0.8,en;q=0.6',
    'HTTP_CACHE_CONTROL': 'max-age=0',
    'HTTP_CONNECTION': 'keep-alive',
    'HTTP_HOST': '127.0.0.1:8080',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux i686)',
    'QUERY_STRING': '',
    'REMOTE_ADDR': '127.0.0.1',
    'REQUEST_METHOD': 'GET',
    'SCRIPT_NAME': '',
    'SERVER_NAME': 'localhost',
    'SERVER_PORT': '8080',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'uwsgi.node': 'localhost',
    'uwsgi.version': '1.2.6',
    'wsgi.errors': None,
    'wsgi.file_wrapper': None,
    'wsgi.input': BytesIO(b""),
    'wsgi.multiprocess': False,
    'wsgi.multithread': False,
    'wsgi.run_once': False,
    'wsgi.url_scheme': 'http',
    'wsgi.version': (1, 0),
}

sections = ["section%d" % i for i in range(10)]

features = ["feature%d" % i for i in range(20)]
