import web


urls = ("/welcome", "welcome")
app = web.application(urls, globals())
main = app.wsgifunc()

class welcome:

    def GET(self):
        return 'Hello World!'
