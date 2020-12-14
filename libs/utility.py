import pandas as pd


class Node(object):
    def __init__(self, tag=None, parent=None, children=list, data=None):
        self.tag = tag
        self.children = children if isinstance(children, list) else [children]
        self.parent = parent
        self.data = data


class Route:
    self.data = list

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __and__(self, other):
        pass

    def __or__(self, other):
        pass


class Tree(object):
    def __init__(self):
        pass

    def insert(self):
        pass

    def search(self):
        pass
