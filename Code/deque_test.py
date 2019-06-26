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

    def test_push_front(self):
        deque = Deque()

        deque.push_front("a")
        assert deque.size == 1
        assert deque.front.data == "a"
        assert deque.back.data == "a"

        deque.push_front("b")
        assert deque.size == 2
        assert deque.front.data == "b"
        assert deque.back.data == "a"

        deque.push_front("d")
        assert deque.size == 3
        assert deque.front.data == "d"
        assert deque.back.data == "a"
