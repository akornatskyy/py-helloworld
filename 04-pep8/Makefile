.SILENT: env up count pep8 mccabe
.PHONY: env up count pep8 mccabe

all: env up count pep8

env:
	if [ ! -d env ]; then \
		virtualenv env ; env/bin/easy_install -O2 pep8 "flake8<1.6"; \
	fi

up:
	if [ ! -d bottle ]; then git clone git://github.com/defnull/bottle.git ; \
		else cd bottle && git pull ; fi
	if [ ! -d cherrypy ]; then hg clone https://bitbucket.org/cherrypy/cherrypy ; \
		else cd cherrypy && hg pull -u ; fi
	if [ ! -d circuits ]; then hg clone https://bitbucket.org/prologic/circuits ; \
		else cd circuits && hg pull -u ; fi
	if [ ! -d django ]; then git clone git://github.com/django/django.git ; \
		else cd django && git pull ; fi
	if [ ! -d tornado ]; then git clone git://github.com/facebook/tornado.git ; \
		else cd tornado && git pull ; fi
	if [ ! -d webpy ]; then git clone git://github.com/webpy/webpy.git ; \
		else cd webpy && git pull ; fi
	if [ ! -d web2py ]; then git clone git://github.com/web2py/web2py.git ; \
		else cd web2py && git pull ; fi
	if [ ! -d pysi ]; then hg clone https://bitbucket.org/imbolc/pysi ; \
		else cd pysi && hg pull -u ; fi
	if [ ! -d turbogears ]; then git clone git://github.com/TurboGears/tg2.git turbogears ; \
		else cd turbogears && git pull ; fi

	if [ ! -d flask ]; then git clone git://github.com/mitsuhiko/flask.git ; \
		else cd flask && git pull ; fi
	if [ ! -d werkzeug ]; then git clone git://github.com/mitsuhiko/werkzeug.git ; \
		else cd werkzeug && git pull ; fi
	if [ ! -d jinja2 ]; then git clone git://github.com/mitsuhiko/jinja2.git ; \
		else cd jinja2 && git pull ; fi

	if [ ! -d pyramid ]; then git clone git://github.com/Pylons/pyramid.git ; \
		else cd pyramid && git pull ; fi
	if [ ! -d chameleon ]; then git clone git://github.com/malthe/chameleon.git ; \
		else cd chameleon && git pull ; fi
	if [ ! -d webob ]; then git clone git://github.com/Pylons/webob.git ; \
		else cd webob && git pull ; fi

	for r in caching core html http routing security template validation web; do \
		r="wheezy."$$r ; \
		if [ ! -d $$r ]; then hg clone https://bitbucket.org/akorn/$$r ; \
		else cd $$r && hg pull -u && cd ..; fi \
	done

count:
	echo "\nnumber of source lines:"
	for r in `ls -d ./*/ | cut -d / -f 2 | grep -v env | sort`; do \
		echo -n "$$r => "; \
		find $$r/ -name '*.py' | xargs wc -l | grep total | cut -d t -f 1; \
	done

pep8: env
	echo "\nnumber of PEP8 errors or warnings:"
	# save your time
	#if [ -f web2py/gluon/contrib/populate.py ]; then \
	#	rm web2py/gluon/contrib/populate.py; \
	#fi
	for r in `ls -d ./wheezy.*/ | cut -d / -f 2 | grep -v env | sort`; do \
		echo -n "$$r => "; \
		env/bin/pep8 --count -qq --ignore=E501,E231,W293,W291 $$r; \
		if [ $$? = "0" ]; then echo 0; fi \
	done ; \
	exit 0

mccabe:
	# this cause an error in falke8
	rm -rf web2py/gluon/contrib/markmin/ ; \
	echo "\nnumber of McCabe errors and overal complexity:"
	for r in `ls -d ./*/ | cut -d / -f 2 | grep -v env | sort`; do \
		echo -n "$$r => "; \
		r=`env/bin/flake8 --max-complexity 10 $$r | grep W901 | \
			cut -d\( -f2 | cut -d\) -f1` ; \
		if [ -z "$$r" ]; then echo 0 0; \
		else echo "$$r" | awk '{c+=1;s+=$$1} END {print c, s}'; fi \
	done ; \
	exit 0
