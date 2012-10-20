

class User(object):

    def __init__(self, name):
        self.name = name


class Item(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price


user = User("John Smith")
items = [Item("apples", "$0.99"), Item("oranges", "$2.49")] * 5
