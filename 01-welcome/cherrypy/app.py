import sys
sys.stdout = sys.stderr

import atexit
import cherrypy


cherrypy.config.update({'environment': 'embedded'})

if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)


class Root(object):

    def welcome(self):
        return 'Hello World!'

    welcome.exposed = True


main = cherrypy.Application(Root(), script_name=None, config=None)
