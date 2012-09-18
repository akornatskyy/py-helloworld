.SILENT: clean env
.PHONY: clean env

VERSION=2.7
PYPI=http://pypi.python.org/simple
ENV=env

PYTHON=$(ENV)/bin/python$(VERSION)
EASY_INSTALL=$(ENV)/bin/easy_install-$(VERSION)


env:
	PYTHON_EXE=/usr/local/bin/python$(VERSION); \
	if [ ! -x $$PYTHON_EXE ]; then \
		    PYTHON_EXE=/usr/bin/python$(VERSION); \
	fi;\
	virtualenv --python=$$PYTHON_EXE env
	$(EASY_INSTALL) -i $(PYPI) -O2 uwsgi django

clean:
	find ./ -type d -name __pycache__ | xargs rm -rf
	find ./ -name '*.py[co]' -delete
