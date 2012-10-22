import tornado.web


class Greeting(tornado.web.UIModule):

    def __init__(self, loader):
        self.loader = loader

    def __call__(self, **ctx):
        template = self.loader.load('uimodules/greeting.html')
        return template.generate(**ctx)


class Greetings(tornado.web.UIModule):

    def __init__(self, loader):
        self.loader = loader

    def __call__(self, **ctx):
        template = self.loader.load('uimodules/greetings.html')
        return template.generate(**ctx)
