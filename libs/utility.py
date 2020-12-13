import pandas as pd


class Node(object):
    def __init__(self, tag=None, parent=None, children=list, data=None):
        self.tag = tag
        self.children = children if isinstance(children, list) else [children]
        self.parent = parent
        self.data = data


class Tree(object):
    def __init__(self):
        pass
