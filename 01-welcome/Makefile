.SILENT: clean env pypy django flask pyramid web.py bottle wheezy.web tornado web2py bobo cherrypy wsgi circuits turbogearsi pysi
.PHONY: clean env pypy django flask pyramid web.py bottle wheezy.web tornado web2py bobo cherrypy wsgi circuits turbogears pysi

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

	if [ ! -f web2py_src.zip ]; then \
		wget http://www.web2py.com/examples/static/web2py_src.zip; \
	fi; \
	rm -rf web2py/web2py ; unzip -qo web2py_src.zip -d web2py/ ; \
	rm -rf web2py/web2py/applications ; \
	mkdir -p web2py/web2py/applications/welcome/controllers
	ln -s `pwd`/web2py/default.py `pwd`/web2py/web2py/applications/welcome/controllers/default.py

	if [ "$$(echo $(VERSION) | sed 's/\.//')" -lt 30 ]; then \
		cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) -O2 \
			"uwsgi>=1.2.6" "gunicorn>=0.14.6" "django>=1.4.1" "flask>=0.9" \
			"pyramid>=1.4a2" "web.py>=0.37" "bottle>=0.10.11" \
			"wheezy.web>=0.1.304" "tornado>=2.4" "bobo>=1.0.0" \
			"cherrypy>=3.2.2" "pysi>=0.13.0" "circuits>=1.6"; \
	else \
		cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) \
				"distribute>=0.6.28" \
			&& ./easy_install-$(VERSION) -i $(PYPI) -O2 \
		   		"uwsgi>=1.3" "pyramid>=1.4a2" "bottle>=0.10.11" \
				"wheezy.web>=0.1.304" "tornado>=2.4" "circuits>=1.6" ; \
	fi

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
		"pyramid>=1.4a2" "web.py>=0.37" "bottle>=0.10.11" \
		"wheezy.web>=0.1.304" "tornado>=2.4" "bobo>=1.0.0" \
		"cherrypy>=3.2.2" "pysi>=0.13.0" "circuits>=1.6"


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

tornado:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini tornado/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:tornado ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

web2py:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini web2py/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:web2py/web2py ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 wsgihandler:application
endif

bobo:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini bobo/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:bobo ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

cherrypy:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini cherrypy/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:cherrypy ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

wsgi:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini wsgi/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:wsgi ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

circuits:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini circuits/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:circuits ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif

turbogears:
	$(ENV)/bin/easy_install-$(VERSION) -i $(PYPI) -O2 \
			"tg.devtools>=2.2.0" "webob==1.1.1"; \
	cd turbogears ; rm -rf helloworld ; \
	../env/bin/paster quickstart -n -x --noinput helloworld ; \
	cd helloworld ; ../../env/bin/python$(VERSION) setup.py develop ; \
	cp ../root.py helloworld/controllers ; \
	cp ../development.ini .

ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini turbogears/uwsgi.ini
else
	$(ENV)/bin/gunicorn_paster -b 0.0.0.0:8080 -w 4 `pwd`/turbogears/helloworld/development.ini
endif

pysi:
ifeq ($(SERVER),uwsgi)
	$(ENV)/bin/uwsgi --ini pysi/uwsgi.ini
else
	export PYTHONPATH=$$PYTHONPATH:pysi ; \
	$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 4 app:main
endif
