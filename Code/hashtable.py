#!python

from linkedlist import LinkedList


class HashTable(object):
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ["{!r}: {!r}".format(key, val) for key, val in self.items()]
        return "{" + ", ".join(items) + "}"

    def __repr__(self):
        """Return a string representation of this hash table."""
        return "HashTable({!r})".format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """
            Return the load factor, the ratio of number of entries to buckets.
            Best and worst case running time: O(1) - Because the calculation is always
            constant.
        """
        return self.size / len(self.buckets)

    def keys(self):
        """
            Return a list of all keys in this hash table.
            Best and worst case running time: O(n) - Where n is the number
            of keys we have within our hashtable
        """
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """
            Return a list of all values in this hash table.
            Best and worst case running time: O(n) - Where n is the number of values 
            within our hashtable
        """
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """
            Return a list of all entries (key-value pairs) in this hash table.
            Best and worst case running time: O(n) - Where n is the number of items
            within our hashtable
        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """
            Return the number of key-value entries by traversing its buckets.
            Best and worst case running time: O(n) - Where n is the number of items
            within our hash table
        """
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets:
            item_count += bucket.length()
        return item_count
        # Equivalent to this list comprehension:
        return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):
        """
            Return True if this hash table contains the given key, or False.
            Best case running time: O(1) - Where there is only one or no items within our bucket.
            Worst case running time: O(l) - Where there is l items within our bucket that have to b
            be checked 
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """
            Return the value associated with the given key, or raise KeyError.
            Best case running time: O(1) - Where there is only one or no items within our bucket.
            Worst case running time: O(l) - Where there are l items within our bucket that have to be checked.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError("Key not found: {}".format(key))

    def set(self, key, value):
        """
            Insert or update the given key with its associated value.
            Best case running time: O(1) - Where there are no other items in the current
            bucket we're indexing into
            Worst case running time: O(l) - Where there are other items in the bucket that we're
            indexing into and l is the load factor of our hash table
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        self.size += 1

        # Check if the load factor exceeds .75, if so resize our hashtable.
        if self.load_factor() > 0.75:
            doubled_size = 2 * len(self.buckets)
            self._resize(new_size=doubled_size)

    def delete(self, key):
        """
            Delete the given key and its associated value, or raise KeyError.
            Best case running time: O(1) - If there is no item or only one item
            in the bucket we're trying to delete from
            Worst case running time: O(l) where l is the load factor of our hash table and
            there are multiple items in the bucket we're trying to insert into
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError("Key not found: {}".format(key))

    def _resize(self, new_size=None):
        """
            Resize this hash table's buckets and rehash all key-value entries.
            Should be called automatically when load factor exceeds a threshold
            such as 0.75 after an insertion (when set is called with a new key).
            Best and worst case running time: O(b) - Where b is the total number of buckets we have
            to create.
            Best and worst case space usage: O(n) - Where n is the total number of entries we have to
            store for when we create new buckets.
        """
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size

        # grab all items from the current hashtable
        all_items = self.items()

        # Reinitialize hashtable
        self.__init__(new_size)

        # insert all items into the new bucket
        for key, value in all_items:
            self.set(key, value)


class LinearHashTable(object):
    """
        Hashtable implemented with linear probing.
    """

    def __init__(self, init_size=8):
        self.buckets = [(None, None) for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ["{!r}: {!r}".format(key, val) for key, val in self.items()]
        return "{" + ", ".join(items) + "}"

    def __repr__(self):
        """Return a string representation of this hash table."""
        return "HashTable({!r})".format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def keys(self):
        """
            Iterate through all of the keys.

            Returns:
                A list of the keys within the hashtable
        """
        all_keys = []
        for key, _ in self.buckets:
            if key is not None:
                all_keys.append(key)

        return all_keys

    def values(self):
        """
            Iterate through all of the values within the hashtable.

            Returns:
                A list of all values within the hashtable.
        """
        all_values = []
        for key, value in self.buckets:
            if key is not None:
                all_values.append(value)

        return all_values

    def items(self):
        """
            Iterate through all of our items within the hashtable.

            Returns:
                A list of all items within the hashtable
        """
        all_items = []
        for key, value in self.buckets:
            if key is not None:
                all_items.append(key, value)

        return all_items

    def length(self):
        """
            Obtain the length or amount of items within the hashtable
            by iterating through it.

            Returns:
                The amount of items within the hashtable
        """
        count = 0
        for key, _ in self.buckets:
            if key is not None:
                count += 1

        return count

    def contains(self, key):
        """
            Check if a key exists within our hashtable

            Returns:
                True if the key is found, False if not.
        """
        index = self._bucket_index(key)

        desired_key, _ = self.buckets[index]

        return key == desired_key

    def get(self, key):
        index = self._bucket_index(key)

        key_at_index, value_at_index = self.buckets[index]
        if not key == key_at_index:
            search_index = index + 1
            while search_index != index:
                if search_index == len(self.buckets) - 1:
                    search_index = 0
                key_at_index, value_at_index = self.buckets[index]

                if key == key_at_index:
                    raise ValueError("Key not within hashtable: {key}")

            return None
        else:
            return value_at_index

    def set(self, key, value):
        index = 

    def delete(self, key):
        pass

    def _load_factor(self):
        return self.size / len(self.buckets)

    def _resize(self, new_size=None):
        pass


def test_hash_table():
    ht = HashTable(4)
    print("HashTable: " + str(ht))

    print("Setting entries:")
    ht.set("I", 1)
    print("set(I, 1): " + str(ht))
    ht.set("V", 5)
    print("set(V, 5): " + str(ht))
    print("size: " + str(ht.size))
    print("length: " + str(ht.length()))
    print("buckets: " + str(len(ht.buckets)))
    print("load_factor: " + str(ht.load_factor()))
    ht.set("X", 10)
    print("set(X, 10): " + str(ht))
    ht.set("L", 50)  # Should trigger resize
    print("set(L, 50): " + str(ht))
    print("size: " + str(ht.size))
    print("length: " + str(ht.length()))
    print("buckets: " + str(len(ht.buckets)))
    print("load_factor: " + str(ht.load_factor()))

    print("Getting entries:")
    print("get(I): " + str(ht.get("I")))
    print("get(V): " + str(ht.get("V")))
    print("get(X): " + str(ht.get("X")))
    print("get(L): " + str(ht.get("L")))
    print("contains(X): " + str(ht.contains("X")))
    print("contains(Z): " + str(ht.contains("Z")))

    print("Deleting entries:")
    ht.delete("I")
    print("delete(I): " + str(ht))
    ht.delete("V")
    print("delete(V): " + str(ht))
    ht.delete("X")
    print("delete(X): " + str(ht))
    ht.delete("L")
    print("delete(L): " + str(ht))
    print("contains(X): " + str(ht.contains("X")))
    print("size: " + str(ht.size))
    print("length: " + str(ht.length()))
    print("buckets: " + str(len(ht.buckets)))
    print("load_factor: " + str(ht.load_factor()))


if __name__ == "__main__":
    test_hash_table()
