#!python


class BinaryTreeNode(object):
    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return "BinaryTreeNode({!r})".format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.left is not None or self.right is not None

    def height(self):
        """
            Return the height of this node (the number of edges on the longest
            downward path from this node to a descendant leaf node).
            Best case: O(1) where the current node is a leaf and no traversing
            is required.
            Worst case: O(n) where we're starting from the root node and have to
            traverse the entire tree to figure out the height.
        """

        # If the current node is a leaf, the height is zero
        if self.is_leaf():
            return 0

        # Initialize our height properties
        left_height = 0
        right_height = 0

        # Check the left side of the node
        if self.left is not None:
            left_height = self.left.height()

        # Check the right side of the node
        if self.right is not None:
            right_height = self.right.height()

        # Obtain the largest value, add one, and then return it.
        largest_height = max(left_height, right_height) + 1
        return largest_height


class BinarySearchTree(object):
    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return "BinarySearchTree({} nodes)".format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """
            Return the height of this tree (the number of edges on the longest
            downward path from this tree's root node to a descendant leaf node).

            Best case: O(1) If the binary tree isn't defined yet or there is only a root
            node.
            Worst case: O(n) Where we have to traverse the entire list of nodes to find the height
        """
        if not self.root:
            return 0

        if self.root.is_leaf():
            return 0

        return self.root.height()

    def contains(self, item):
        """
            Return True if this binary search tree contains the given item.
            TODO: Best case running time: O(1) - Where the node we're looking for
            is the root node.
            TODO: Worst case running time: O(logn) - Where the node we're looking for is a leaf node
            or simply doesn't exist
        """
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """
            Return an item in this binary search tree matching the given item,
            or None if the given item is not found.
            TODO: Best case running time: O(1) - Where the node we're looking for is the root node or
            the tree hasn't been setup.
            TODO: Worst case running time: O(logn) Where the node we're looking for is a leaf node
            or simply doesn't exist
        """
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        return node.data if node else None

    def insert(self, item):
        """
            Insert the given item in order into this binary search tree.
            TODO: Best case running time: O(1) where the tree is empty
            TODO: Worst case running time: O(logn) where we have to insert towards the middle
            or end of the tree
        """
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)

        # Check where to insert the node
        if parent.data > item:
            parent.left = BinaryTreeNode(item)
        elif parent.data < item:
            parent.right = BinaryTreeNode(item)
        self.size += 1

    def _find_node_iterative(self, item):
        """
            Return the node containing the given item in this binary search tree,
            or None if the given item is not found. Search is performed iteratively
            starting from the root node.
            TODO: Best case running time: O(1) - Where the tree is empty or contains only one node.
            TODO: Worst case running time: O(logn) - Where the node we're looking for is towards the bottom
            of the tree or cant be found
        """

        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data == item:
                return node
            elif node.data > item:
                node = node.left
            elif node.data < item:
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """
            Return the node containing the given item in this binary search tree,
            or None if the given item is not found. Search is performed recursively
            starting from the given node (give the root node to start recursion).
            TODO: Best case running time: O(1) - Where the tree is empty or contains only one node.
            TODO: Worst case running time: O(logn) - Where the node we're looking for is towards the bottom
            of the tree or cant be found
        """
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        elif node.data == item:
            # Return the found node
            return node
        elif node.data > item:
            return self._find_node_recursive(item, node.left)
        else:
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """
            Return the parent node of the node containing the given item
            (or the parent node of where the given item would be if inserted)
            in this tree, or None if this tree is empty or has only a root node.
            Search is performed iteratively starting from the root node.
            TODO: Best case running time: O(1) - Where the tree is empty or contains only one node.
            TODO: Worst case running time: O(logn) - Where the node we're looking for is towards the bottom
            of the tree or cant be found

        """
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data == item:
                return parent
            elif node.data > item:
                parent = node
                node = node.left
            elif node.data < item:
                parent = node
                node = node.right
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """
            Return the parent node of the node containing the given item
            (or the parent node of where the given item would be if inserted)
            in this tree, or None if this tree is empty or has only a root node.
            Search is performed recursively starting from the given node
            (give the root node to start recursion).
            TODO: Best case running time: O(1) - Where the tree is empty or contains only one node.
            TODO: Worst case running time: O(logn) - Where the node we're looking for is towards the bottom
        """
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        if node.data == item:
            # Return the parent of the found node
            return parent
        elif node.data > item:
            if not node.left:
                return node

            return self._find_parent_node_recursive(
                item, node.left, parent=node
            )  # Hint: Remember to update the parent parameter
        elif node.data < item:
            if not node.right:
                return node
            return self._find_parent_node_recursive(
                item, node.right, parent=node
            )  # Hint: Remember to update the parent parameter

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        parent_node = self._find_parent_node_recursive(item, self.root)

        if parent_node:
            self.size -= 1

            # Start removal
            if parent_node.data > item:
                node_to_remove = parent_node.left

                # No children leafs, sever node off
                if node_to_remove.is_leaf():
                    parent_node.left = None
                    return

                # If the right node is present, move it up to the new node.
                # If it's not, move up the left node. Essentially moves up the next
                # greatest value.
                if node_to_remove.right:
                    parent_node.left = node_to_remove.right
                else:
                    parent_node.left = node_to_remove.left
            else:
                node_to_remove = parent_node.right

                if node_to_remove.is_leaf():
                    parent_node.left = None
                    return

                # If the left node is present, move it up to the new node.
                # If it's not, move up the right node. Essentially moves up the next
                # greatest value.
                if node_to_remove.left:
                    parent_node.right = node_to_remove.left
                else:
                    parent_node.right = node_to_remove.right

        # Root node doesn't have a parent node, but can contain item
        # we're looking for.
        elif parent_node is None and self.root.data == item:
            self.size -= 1
            self.root == None
        else:
            raise ValueError("Node is not located within the binary tree")
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Because we have to traverse every single node
        TODO: Memory usage: O(1) Because we're just traversing the tree and visiting 
        the data is at each node.
        """
        # Traverse the left side all the way down
        if node.left:
            self._traverse_in_order_recursive(node.left, visit)

        visit(node.data)

        # Traverse the right side all the way down
        if node.right:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """
            Traverse this binary tree with iterative in-order traversal (DFS).
            Start at the given node and visit each node with the given function.
            TODO: Running time: O(n) - Where n is the number of nodes that we have to traverse.
            TODO: Memory usage: O(m) - Where m is a subset of the nodes that will be kept in the stack
            at any given time.
        """
        stack = list()
        while stack or node is not None:
            # If the node isn't none, append it to the stack
            # and progress to the left
            if node:
                stack.append(node)
                node = node.left
            # Else, pop the previous node, visit it, and then move to the right.
            else:
                node = stack.pop()
                visit(node.data)

                node = node.right

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) - Where n is the number of nodes that we have to traverse
        TODO: Memory usage: O(1) - Because we don't create any data structures within the alg.
        """
        visit(node.data)

        if node.left:
            self._traverse_pre_order_recursive(node.left, visit)

        if node.right:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O()
        TODO: Memory usage: ??? Why and under what conditions?"""
        stack = list()
        while stack or node is not None:
            if node:
                visit(node.data)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_iterative(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node.left:
            self._traverse_post_order_recursive(node.left, visit)

        if node.right:
            self._traverse_post_order_recursive(node.right, visit)

        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)
        stack = list()
        while stack or node is not None:
            # If the node exists, keep going left
            if node:
                stack.append(node)
                node = node.left
            else:
                # Peek into our stacks right node
                temp = stack[-1].right

                # If there is on right node...
                if temp is None:
                    # Pop the top of the stack and visit it's data
                    temp = stack.pop()
                    visit(temp.data)

                    # While the stack remains and the previous stack top is
                    # equal to the right of the current stacks top, visit the data.
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        visit(temp.data)
                else:
                    # Otherwise, node becomes the right side of the current stack
                    node = temp

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""

        # # TODO: Create queue to store nodes not yet traversed in level-order
        # queue = ...
        # # TODO: Enqueue given starting node
        # # TODO: Loop until queue is empty
        # while ...:
        #     # TODO: Dequeue node at front of queue
        #     node = ...
        #     # TODO: Visit this node's data with given function
        #     ...
        #     # TODO: Enqueue this node's left child, if it exists
        #     ...
        #     # TODO: Enqueue this node's right child, if it exists
        #     ...
        pass


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print("items: {}".format(items))

    tree = BinarySearchTree()
    print("tree: {}".format(tree))
    print("root: {}".format(tree.root))

    print("\nInserting items:")
    for item in items:
        tree.insert(item)
        print("insert({}), size: {}".format(item, tree.size))
    print("root: {}".format(tree.root))

    print("\nSearching for items:")
    for item in items:
        result = tree.search(item)
        print("search({}): {}".format(item, result))
    item = 123
    result = tree.search(item)
    print("search({}): {}".format(item, result))

    print("\nTraversing items:")
    print("items in-order:    {}".format(tree.items_in_order()))
    print("items pre-order:   {}".format(tree.items_pre_order()))
    print("items post-order:  {}".format(tree.items_post_order()))
    print("items level-order: {}".format(tree.items_level_order()))


if __name__ == "__main__":
    test_binary_search_tree()
