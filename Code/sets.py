from hashtable import HashTable


class HashTableSet(HashTable):
    def __init__(self, items=None):
        super().__init__()
        # Add initial items
        if items is not None:
            for item in items:
                self.add(item)

    def __contains__(self, item):
        return self.contains(item)

    def add(self, key: object):
        """
            Add an item to the Set.
            Runtime: O(1) average - Because we hash the key to find the desired
            bucket to store it in and then store it in our hashtable, which are all
            O(1) operations.
        """
        self.set(key, None)

    def remove(self, key: object):
        """
            Delete an item from the Set.
            Runtime: O(1) average - Because we hash the key to find the bucket
            that it the key would be stored in and then proceed to remove it if possible,
            which consists of all O(1) operations.
        """
        self.delete(key)

    def items(self):
        """
            Wrapper function to overwrite items to also provide us just
            the keys of our set
        """
        return self.keys()

    def union(self, other_set: "HashTableSet") -> "HashTableSet":
        """
            Obtains all the elements that are in both this set and another one..
            Runtime: O(n) where n is the number of items within the larger set.

            Params:
                other_set - A HashTableSet object that we're trying to compare to

            Returns:
                a new set that contains all the items in both this set and the other one.
        """
        assert isinstance(
            other_set, HashTableSet
        ), "You must provide HashTableSet object"

        union_set = HashTableSet()

        # Iterate through the items of this set, adding them into the
        # union set we craeted.
        for item in self.items():
            union_set.add(item)

        # Iterate through the items of the other set, adding them into
        # the union set we creatd
        for item in other_set.items():
            union_set.add(item)

        return union_set

    def intersection(self, other_set: "HashTableSet") -> "HashTableSet":
        """
            Obtain a new set that contains the intersection amongst this set
            and another set
            Runtime: O(n) where n is the number of items within this set.

            Params:
                other_set - A HashTableSet object to be checked against.

            Returns:
                A new set that contains the intersection between this set and
                the other one.
        """
        assert isinstance(other_set, HashTableSet), "You must proivide a Hashtable set"
        intersection_set = HashTableSet()

        # Iterate through the items from this set and check if they're in the other set.
        # Add them if so (intersection)
        for item in self.items():
            if item in other_set:
                intersection_set.add(item)

        return intersection_set

    def difference(self, other_set: "HashTableSet") -> "HashTableSet":
        """
            Obtain a new set that contains the differences amongst this set
            and another set.
            Runtime: O(n) where n is the number of items in whichever set is larger and
            contains more entries.

            Params:
                other_set - A HashTableSet object we're checking against.

            Returns:
                A new set containing the difference between this set and the other set.
        """
        assert isinstance(other_set, HashTableSet), "You must provide a hashtable set"
        difference_set = HashTableSet()

        for item in self.items():
            if item not in other_set:
                difference_set.add(item)

        return difference_set

    def is_subset(self, other_set: "HashTableSet") -> bool:
        """
            Check if another set is a subset of this current set
            Runtime O(n) where n is the amount of items within the other hash
            table.

            Params:
                other_set - A HashTableSet object

            Returns:
                True if the other set is a subset of the current set
                False if the other set is not a subset of the current set
        """

        if other_set.size == 0:
            return True
        else:
            for item in other_set.items():
                if item not in self:
                    return False
            return True
