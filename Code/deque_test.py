import unittest

from deque import Deque


class DequeTest(unittest.TestCase):
    def test_init(self):
        deque = Deque()
        assert deque.is_empty() == True
        assert deque.size == 0

        deque = Deque(["a", "b", "c"])
        assert deque.is_empty() == False
        assert deque.size == 3
