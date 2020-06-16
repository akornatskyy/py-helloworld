
"""
"""

from django import template
# from django.template import Context
from django.template import Library
from django.template import Node
from django.template import Variable
from django.template import loader
# from django.template.defaulttags import register


class GreetingNode(Node):

    def __init__(self, name):
        self.name = Variable(name)
        self.template = loader.get_template('tags/greeting.html')

    def render(self, context):
        return self.template.render({
            'name': self.name.resolve(context)
        })


class GreetingsNode(Node):

    def __init__(self, names):
        self.names = Variable(names)
        self.template = loader.get_template('tags/greetings.html')

    def render(self, context):
        return self.template.render({
            'names': self.names.resolve(context)
        })


def build_tag(node_class):
    def tag(parser, token):
        _, name = token.split_contents()
        return node_class(name)
    return tag


register = template.Library()
register.tag('greeting', build_tag(GreetingNode))
register.tag('greetings', build_tag(GreetingsNode))
