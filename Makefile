.SILENT: clean env django
.PHONY: clean env django

VERSION=2.7
PYPI=http://pypi.python.org/simple
ENV=env

PYTHON=$(ENV)/bin/python$(VERSION)


env:
	PYTHON_EXE=/usr/local/bin/python$(VERSION); \
	if [ ! -x $$PYTHON_EXE ]; then \
		    PYTHON_EXE=/usr/bin/python$(VERSION); \
	fi;\
	virtualenv --python=$$PYTHON_EXE --no-site-packages env
	cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) -O2 \
		uwsgi django

clean:
	find ./ -type d -name __pycache__ | xargs rm -rf
	find ./ -name '*.py[co]' -delete

django:
	$(ENV)/bin/uwsgi --ini django/uwsgi.ini
