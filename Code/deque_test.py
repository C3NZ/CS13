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
        assert deque.front() == "a"
        assert deque.back() == "a"

        deque.push_front("b")
        assert deque.size == 2
        assert deque.front() == "b"
        assert deque.back() == "a"

        deque.push_front("d")
        assert deque.size == 3
        assert deque.front() == "d"
        assert deque.back() == "a"

    def test_push_back(self):
        deque = Deque()

        deque.push_back("a")
        assert deque.size == 1
        assert deque.front() == "a"
        assert deque.back() == "a"

        deque.push_back("b")
        assert deque.size == 2
        assert deque.front() == "a"
        assert deque.back() == "b"

        deque.push_back("c")
        assert deque.size == 3

        assert deque.front() == "a"
        assert deque.back() == "c"

    def test_pop_front(self):
        deque = Deque(["a", "b", "c"])
        assert deque.size == 3
        assert deque.front() == "a"
        assert deque.back() == "c"

        assert deque.pop_front() == "a"
        assert deque.size == 2
        assert deque.front() == "b"
        assert deque.back() == "c"

        assert deque.pop_front() == "b"
        assert deque.size == 1
        assert deque.front() == "c"
        assert deque.back() == "c"

        assert deque.pop_front() == "c"
        assert deque.size == 0
        assert deque.front() == None
        assert deque.back() == None
