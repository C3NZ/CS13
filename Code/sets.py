from hashtable import HashTable


class HashTableSet(HashTable):
    def __init__(self, items=None):
        super().__init__()
        # Add initial items
        if items is not None:
            for item in items:
                self.add(item)

    def add(self, key: object):
        """
            Add an item to the Set.
        """
        self.set(key, None)

    def remove(self, key: object):
        """
            Delete an item from the Set.
        """
        self.delete(key)
