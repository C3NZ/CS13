import unittest
from sets import HashTableSet


class SetsTest(unittest.TestCase):
    def test_init(self):
        hts = HashTableSet()
        assert hts.size == 0

        hts = HashTableSet(["yes", "indeed", "setter"])
        assert hts.size == 3

    def test_contains(self):
        hts = HashTableSet(["yes", "no", "yessir"])
        assert hts.size == 3

        assert hts.contains("yes") is True
        assert hts.contains("Yes") is False
        assert hts.contains("YES") is False

        assert hts.contains("no") is True
        assert hts.contains("nO") is False
        assert hts.contains("noo") is False

        assert hts.contains("yessir") is True
        assert hts.contains("yesssir") is False

    def test_add(self):
        hts = HashTableSet()

        hts.add("B")
        assert hts.size == 1
        assert hts.contains("B") is True

        hts.add("c")
        assert hts.size == 2
        assert hts.contains("c") is True

        hts.add("c")
        assert hts.size == 2
        assert hts.contains("c") is True

        hts.add("yoo")
        assert hts.size == 3
        assert hts.contains("yoo") is True

    def test_remove(self):
        hts = HashTableSet()
        hts.add("yes")
        hts.add("no")
        hts.add("maybeso")

        assert hts.size == 3
        assert hts.contains("yes") is True
        hts.remove("yes")
        assert hts.contains("yes") is False

        assert hts.size == 2
        assert hts.contains("no") is True
        # Expect a key error when trying to remove prev element
        with self.assertRaises(KeyError):
            hts.remove("yes")
        hts.remove("no")
        assert hts.contains("no") is False

        assert hts.size == 1
        assert hts.contains("maybeso") is True
        hts.remove("maybeso")
        assert hts.contains("maybeso") is False

    def test_contains(self):
        hts = HashTableSet(["yes", "no", "yessir"])
        assert hts.size == 3

        assert hts.contains("yes") is True
        assert hts.contains("Yes") is False
        assert hts.contains("YES") is False
