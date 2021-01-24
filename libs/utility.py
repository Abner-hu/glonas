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
    def __init__(self, rootdata):
        self.root = Node(data=rootdata)

    @staticmethod
    def insert(parent, children):
        children.parent = parent
        parent.children.append(children)

    def search(self, node, data):
        if node.data == data:
            return node
        elif len(node.children) == 0:
            return None
        for child in node.children:
            result = self.search(child, data)
            if result:
                return result
        return None
