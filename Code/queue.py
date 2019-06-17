#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return "Queue({} items, front={})".format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty

        return self.list.is_empty()

    def length(self):
        """
            Return the number of items in this queue.
            Running time: O(1) - we keep track of our linked list with a size property
        """
        # TODO: Count number of items
        return self.list.size

    def enqueue(self, item):
        """
            Insert the given item at the back of this queue.
            Running time: O(1) - Appending to a linkedlist is a constant time
            operation
        """
        self.list.append(item)

    def front(self):
        """
            Return the item at the front of this queue without removing it,
            or None if this queue is empty.
            Running time: O(1) - Constant time operation to check the length
            and to get the first element within a linked list.
        """
        if self.is_empty():
            return None

        return self.list.get_at_index(0)

    def dequeue(self):
        """
            Remove and return the item at the front of this queue,
            or raise ValueError if this queue is empty.
            Running time: O(1) - checking if empty is constant time and getting and deleting
            the first index inside of our list is also constant time.
        """
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError("The queue is currently empty")

        item = self.list.get_at_index(0)
        self.list.delete(item)
        return item


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return "Queue({} items, front={})".format(self.length(), self.front())

    def is_empty(self):
        """
            Return True if this queue is empty, or False otherwise.
            Runtime: O(1) - Arrays keep track of length
        """
        return len(self.list) == 0

    def length(self):
        """
            Return the number of items in this queue.
            Runtime: O(1) - Arrays keep track of length
        """
        return len(self.list)

    def enqueue(self, item):
        """
            Insert the given item at the back of this queue.
            Running time: O(1) - Barring that inserting an item wont resize the array,
            insertions are constant time operations.
        """
        self.list.append(item)

    def front(self):
        """
            Return the item at the front of this queue without removing it,
            or None if this queue is empty.
            Running time: O(1) - Indexing into a list is a constant time operation
        """
        if self.is_empty():
            return None

        return self.list[0]

    def dequeue(self):
        """
            Remove and return the item at the front of this queue,
            or raise ValueError if this queue is empty.
            Running time: O(n) - Every time we pop from the front we have to shift
            all of the items within the array over 1
        """
        if self.is_empty():
            raise ValueError("The queue is empty")

        return self.list.pop(0)


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
Queue = ArrayQueue
