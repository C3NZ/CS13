from collections import namedtuple

from linkedlist import Node

NODEDATA = namedtuple("Node", ["left", "item"])


class SinglyLinkedTree:
    def __init__(self, items=None):
        """
            Initialize the binary search tree and insert the given items.
        """
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def is_empty(self):
        """
            Is empty function for singly linked tree
        """
        return self.root is None

    def height(self):
        pass

    def contains(self, item):
        pass

    def search(self, item):
        pass

    def insert(self, item):
        if not self.root:
            data = NODEDATA(None, item)
            self.root = Node(data)

    def delete(self, item):
        pass

    def _find_node_recursive(self, item, node):
        pass

    def _find_parent_node_recursive(self, item, node, parent=None):
        pass

    def items_in_order(self):
        pass
