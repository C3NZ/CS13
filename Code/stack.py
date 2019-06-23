#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack:
    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return "Stack({} items, top={})".format(self.length(), self.peek())

    def is_empty(self):
        """
            Return True if this stack is empty, or False otherwise.
        """
        return self.list.is_empty()

    def length(self):
        """
            Return the number of items in this stack.
        """
        return self.list.size

    def push(self, item):
        """
            Insert the given item on the top of this stack.
            Running time: O(1) - Prepending is a constant operation in our linkedlist
        """
        self.list.prepend(item)

    def peek(self):
        """
            Return the item on the top of this stack without removing it,
            or None if this stack is empty.
            Running time: O(1) - Checking the head is always a constant operation
        """
        if self.is_empty():
            return None

        return self.list.get_at_index(0)

    def pop(self):
        """
            Remove and return the item on the top of this stack,
            or raise ValueError if this stack is empty.
            Running time: O(1) – both indexing and deleting the head of a linked list
            will always be running in the same amount of operations
        """
        if self.is_empty():
            raise ValueError("The stack is currently empty")

        # Get the item and then delete it.
        item = self.list.get_at_index(0)
        self.list.delete(item)
        return item


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack:
    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return "Stack({} items, top={})".format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None

        return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        if self.is_empty():
            raise ValueError("The stack is currently empty")

        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
Stack = ArrayStack
