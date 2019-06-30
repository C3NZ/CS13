#!python

import unittest

from hashtable import LinearHashTable

# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, "assertCountEqual"):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):
    def test_init(self):
        ht = LinearHashTable(4)
        assert len(ht.buckets) == 4
        assert ht.length() == 0
        assert ht.size == 0

    def test_keys(self):
        ht = LinearHashTable()
        assert ht.keys() == []
        ht.set("I", 1)
        assert ht.keys() == ["I"]
        ht.set("V", 5)
        self.assertCountEqual(ht.keys(), ["I", "V"])  # Ignore item order
        ht.set("X", 10)
        self.assertCountEqual(ht.keys(), ["I", "V", "X"])  # Ignore item order

    def test_values(self):
        ht = LinearHashTable()
        assert ht.values() == []
        ht.set("I", 1)
        assert ht.values() == [1]
        ht.set("V", 5)
        self.assertCountEqual(ht.values(), [1, 5])  # Ignore item order
        ht.set("X", 10)
        self.assertCountEqual(ht.values(), [1, 5, 10])  # Ignore item order

    def test_items(self):
        ht = LinearHashTable()
        assert ht.items() == []
        ht.set("I", 1)
        assert ht.items() == [("I", 1)]
        ht.set("V", 5)
        self.assertCountEqual(ht.items(), [("I", 1), ("V", 5)])
        ht.set("X", 10)
        self.assertCountEqual(ht.items(), [("I", 1), ("V", 5), ("X", 10)])

    def test_length(self):
        ht = LinearHashTable()
        assert ht.length() == 0
        ht.set("I", 1)
        assert ht.length() == 1
        ht.set("V", 5)
        assert ht.length() == 2
        ht.set("X", 10)
        assert ht.length() == 3

    def test_size(self):
        ht = LinearHashTable()
        assert ht.size == 0
        ht.set("I", 1)
        assert ht.size == 1
        ht.set("V", 5)
        assert ht.size == 2
        ht.set("X", 10)
        assert ht.size == 3

    def test_resize(self):
        ht = LinearHashTable(2)  # Set init_size to 2
        assert ht.size == 0
        assert len(ht.buckets) == 2
        assert ht.load_factor() == 0
        ht.set("I", 1)
        assert ht.size == 1
        assert len(ht.buckets) == 2
        assert ht.load_factor() == 0.5
        ht.set("V", 5)  # Should trigger resize
        assert ht.size == 2
        assert len(ht.buckets) == 4
        assert ht.load_factor() == 0.5
        ht.set("X", 10)
        assert ht.size == 3
        assert len(ht.buckets) == 4
        assert ht.load_factor() == 0.75
        ht.set("L", 50)  # Should trigger resize
        assert ht.size == 4
        assert len(ht.buckets) == 8
        assert ht.load_factor() == 0.5

    def test_contains(self):
        ht = LinearHashTable()
        ht.set("I", 1)
        ht.set("V", 5)
        ht.set("X", 10)
        assert ht.contains("I") is True
        assert ht.contains("V") is True
        assert ht.contains("X") is True
        assert ht.contains("A") is False

    def test_set_and_get(self):
        ht = LinearHashTable()
        ht.set("I", 1)
        ht.set("V", 5)
        ht.set("X", 10)
        ht.set("Y", 12)
        ht.set("R", 23)
        ht.set("YG", 45)
        ht.set("yeet", 300)
        assert ht.get("I") == 1
        assert ht.get("V") == 5
        assert ht.get("X") == 10
        assert ht.get("Y") == 12
        assert ht.get("R") == 23
        assert ht.get("yeet") == 300
        assert ht.get("YG") == 45
        assert ht.length() == 7
        assert ht.size == 7
        with self.assertRaises(KeyError):
            ht.get("A")  # Key does not exist

    def test_set_twice_and_get(self):
        ht = LinearHashTable()
        ht.set("I", 1)
        ht.set("V", 4)
        ht.set("X", 9)
        assert ht.length() == 3
        assert ht.size == 3
        ht.set("V", 5)  # Update value
        ht.set("X", 10)  # Update value
        assert ht.get("I") == 1
        assert ht.get("V") == 5
        assert ht.get("X") == 10
        assert ht.length() == 3  # Check length is not overcounting
        assert ht.size == 3  # Check size is not overcounting

    def test_delete(self):
        ht = LinearHashTable()
        ht.set("I", 1)
        ht.set("V", 5)
        ht.set("X", 10)
        ht.set("Y", 12)
        ht.set("R", 23)
        ht.set("YG", 45)
        ht.set("yeet", 300)

        assert ht.length() == 7
        assert ht.size == 7
        ht.delete("I")
        ht.delete("X")
        ht.delete("Y")
        ht.delete("R")
        ht.delete("yeet")
        assert ht.length() == 2
        assert ht.size == 2
        with self.assertRaises(KeyError):
            ht.delete("X")  # Key no longer exists
        with self.assertRaises(KeyError):
            ht.delete("A")  # Key does not exist


if __name__ == "__main__":
    unittest.main()
