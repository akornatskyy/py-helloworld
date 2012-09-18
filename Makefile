.SILENT: clean env django flask pyramid
.PHONY: clean env django flask pyramid

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
		"uwsgi>=1.2.6" "django>=1.4.1" "flask>=0.9" \
		"pyramid>=1.4a1"

clean:
	find ./ -type d -name __pycache__ | xargs rm -rf
	find ./ -name '*.py[co]' -delete

django:
	$(ENV)/bin/uwsgi --ini django/uwsgi.ini

flask:
	$(ENV)/bin/uwsgi --ini flask/uwsgi.ini

pyramid:
	$(ENV)/bin/uwsgi --ini pyramid/uwsgi.ini
