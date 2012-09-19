.SILENT: clean env pypy django flask pyramid web.py bottle wheezy.web
.PHONY: clean env pypy django flask pyramid web.py bottle wheezy.web

VERSION=2.7
PYPI=http://pypi.python.org/simple
ENV=env

PYTHON=$(ENV)/bin/python$(VERSION)
PYPY=pypy-1.9

SERVER=uwsgi


env:
	PYTHON_EXE=/usr/local/bin/python$(VERSION); \
	if [ ! -x $$PYTHON_EXE ]; then \
		    PYTHON_EXE=/usr/bin/python$(VERSION); \
	fi; \
	virtualenv --python=$$PYTHON_EXE --no-site-packages env
	cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) -O2 \
		"uwsgi>=1.2.6" "gunicorn>=0.14.6" "django>=1.4.1" "flask>=0.9" \
		"pyramid>=1.4a1" "web.py>=0.37" "bottle>=0.10.11" \
		"wheezy.web>=0.1.292"

pypy:
	if [ ! -f $(PYPY)-linux64.tar.bz2 ]; then \
		wget https://bitbucket.org/pypy/pypy/downloads/$(PYPY)-linux64.tar.bz2; \
	fi; \
	tar xjf $(PYPY)-linux64.tar.bz2; \
	wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz; \
	tar xzf setuptools-0.6c11.tar.gz ; \
	cd setuptools-0.6c11 ; \
	../$(PYPY)/bin/pypy setup.py install ; \
	cd .. ; \
	rm -rf setuptools* ; \
	cd $(PYPY)/bin && ./easy_install -i $(PYPI) -O2 \
		"gunicorn>=0.14.6" "flask>=0.9" \
		"pyramid>=1.4a1" "web.py>=0.37" "bottle>=0.10.11" \
		"wheezy.web>=0.1.292"

clean:
	find ./ -type d -name __pycache__ | xargs rm -rf
	find ./ -name '*.py[co]' -delete

django:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini django/uwsgi.ini
else
	echo "Not available"
endif

flask:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini flask/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:flask; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

pyramid:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini pyramid/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:pyramid ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

web.py:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini web.py/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:web.py ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

bottle:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini bottle/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:bottle ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

wheezy.web:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini wheezy.web/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:wheezy.web ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif
