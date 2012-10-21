
"""
"""

from django import template
from django.template import Context
from django.template import Library
from django.template import Node
from django.template import Variable
from django.template import loader


class WelcomeNode(Node):

    def __init__(self, name):
        self.name = Variable(name)
        self.template = loader.get_template('shared/tags/welcome.html')

    def render(self, context):
        return self.template.render(Context({
            'name': self.name.resolve(context)
        }))


class ItemNode(Node):

    def __init__(self, i):
        self.i = Variable(i)
        self.template = loader.get_template('shared/tags/item.html')

    def render(self, context):
        return self.template.render(Context({
            'i': self.i.resolve(context)
        }))


def build_tag(node_class):
    def tag(parser, token):
        tag_name, name = token.split_contents()
        return node_class(name)
    return tag


def register_tags():
    lib = Library()
    lib.tag('welcome', build_tag(WelcomeNode))
    lib.tag('item', build_tag(ItemNode))
    template.builtins.append(lib)
