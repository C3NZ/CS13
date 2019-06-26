from doublylinkedlist import Node


class StrippedDll(object):
    """
        A stripped down doubly linked list optimized specifically for
        fast insertions and deletions within a deque
    """

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ["({!r})".format(item) for item in self.items()]
        return "[{}]".format(" -> ".join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return "LinkedList({!r})".format(self.items())

    def __iter__(self):
        """
            Make the Doubly linked list iterable
        """
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next

    def reversed(self):
        """
            Allow the linked list to be reversed backwards
        """
        curr_node = self.tail
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.prev

    def items(self):
        """
            Return a list of all items in this linked list.
            Best and worst case running time: Theta(n) for n items in the list
            because we always need to loop through all n nodes.
        """
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def append(self, item):
        """
            Insert the given item at the tail of this linked list.
            Best and worst case running time: Omega(1) - Because for however large
            are linkedlist is we're always performing a constant amount of
            operations
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            new_node.prev = self.tail
            self.tail.next = new_node

        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """
            Insert the given item at the head of this linked list.
            Best and worst case running time: O(1) - Constant amount of operations
            regardless of the size of the linked list
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            self.head.prev = new_node
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def delete(self, head=False, tail=False):
        """
            Delete function optimized for deque
        """
        if not (head or tail):
            raise ValueError("Must provide a head or tail to delete")
        elif head and tail:
            raise ValueError("Must provide only a head or tail to delete")

        if self.is_empty():
            raise ValueError("The linked list is currently empty")

        if self.size > 1:
            if head:
                data = self.head.data
                self.head = self.head.next
                self.head.prev = None
                self.size -= 1
                return data
            elif head:
                data = self.tail.data
                self.head = self.head.next
                self.head.prev = None
                self.size -= 1
                return data
        else:
            data = self.head.data
            self.head = None
            self.tail = None
            return data


class Deque(StrippedDll):
    def __init__(self, items):
        super().__init__(items)
        for item in items:
            self.push_back(item)

    def is_empty(self):
        """
            Check if the deque is empty
        """
        return self.is_empty()

    def push_front(self, item):
        """
            Push an item to the front of the deque.
            Runtime: O(1) - Because we're using a doubly linked list
            under the hood to add the item to our deque
        """
        self.prepend(item)

    def push_back(self, item):
        """
            Push an item to the back of the deque.
            Runtime: O(1) - Because we're  using a doubly linked list
            under the hood to add the items to our deque
        """
        self.append(item)

    def pop_front(self):
        """
            Pop an item from the front of the deque.
            Runtime: O(1) - Because we're using a doubly linked list under the hood
            to remove just our head
        """
        return self.delete(head=True)

    def pop_back(self):
        """
            Pop an item from the back of the deque.
            Runtime: O(1) - Because we're using a doubly linked list under the hood to remove
            just our tail
        """
        return self.delete(tail=True)
