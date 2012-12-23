.SILENT: clean env pypy
.PHONY: clean env pypy

VERSION=2.7
PYPI=http://pypi.python.org/simple
ENV=env

PYTHON=$(ENV)/bin/python$(VERSION)
PYPY=pypy-1.9


env:
	PYTHON_EXE=/usr/local/bin/python$(VERSION); \
	if [ ! -x $$PYTHON_EXE ]; then \
		    PYTHON_EXE=/usr/bin/python$(VERSION); \
	fi; \
	virtualenv --python=$$PYTHON_EXE --no-site-packages env

	if [ "$$(echo $(VERSION) | sed 's/\.//')" -lt 30 ]; then \
		cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) -O2 \
			"wheezy.html>=0.1.122" "wheezy.template>=0.1.125" "mako>=0.7.2" \
			"jinja2>=2.6" "django>=1.4.2" "tornado>=2.4" \
			"tenjin>=1.1.1" "webext>=0.0.1" ; \
	else \
		cd $(ENV)/bin && ./easy_install-$(VERSION) -i $(PYPI) \
				"distribute>=0.6.28" \
			&& ./easy_install-$(VERSION) -i $(PYPI) -O2 \
				"wheezy.html>=0.1.122" "wheezy.template>=0.1.125" \
				"mako>=0.7.2" "jinja2>=2.6" "tornado>=2.4"; \
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
		"wheezy.html>=0.1.122" "wheezy.template>=0.1.125" "mako>=0.7.2" \
		"jinja2>=2.6" "tornado>=2.4"

clean:
	find ./ -type d -name __pycache__ | xargs rm -rf
	find ./ -name '*.py[co]' -delete
