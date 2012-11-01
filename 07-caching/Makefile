.SILENT: clean env pypy django flask wheezy.web
.PHONY: clean env pypy django flask wheezy.web

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

	if [ "$$(echo $(VERSION) | sed 's/\.//')" -lt 30 ]; then \
		cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) -O2 \
			"uwsgi>=1.2.6" "gunicorn>=0.14.6" \
			"python-memcached>=1.48" "pylibmc>=1.2.3" \
			"django>=1.4.2" "wheezy.web>=0.1.307" "Flask-Cache>=0.9.0"; \
	else \
		cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) \
				"distribute>=0.6.28" \
			&& ./easy_install-$(VERSION) -i $(PYPI) -O2 \
		   		"uwsgi>=1.3" "python-memcached>=1.48" \
		   		"wheezy.web>=0.1.307" ; \
	fi

pypy:
	if [ `uname -m` = "x86_64" ]; then \
		ARCH='64'; \
	else \
		ARCH=''; \
	fi; \
	if [ ! -f $(PYPY)-linux$$ARCH.tar.bz2 ]; then \
		wget https://bitbucket.org/pypy/pypy/downloads/$(PYPY)-linux$$ARCH.tar.bz2; \
	fi; \
	tar xjf $(PYPY)-linux$$ARCH.tar.bz2; \
	wget http://python-distribute.org/distribute_setup.py ; \
	$(PYPY)/bin/pypy distribute_setup.py ; \
	rm distribute* ; \
	cd $(PYPY)/bin && ./easy_install -i $(PYPI) -O2 \
		"gunicorn>=0.14.6" "python-memcached>=1.48" "wheezy.web>=0.1.307" \
		"Flask-Cache>=0.9.0"

clean:
	find ./ -type d -name __pycache__ | xargs rm -rf
	find ./ -name '*.py[co]' -delete

django:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini django/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:django; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 helloworld.wsgi:application
endif

wheezy.web:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini wheezy.web/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:wheezy.web ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

flask:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini flask/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:flask ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif
