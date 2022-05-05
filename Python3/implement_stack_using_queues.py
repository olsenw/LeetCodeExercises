# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque

'''
Implement a last-in-first-out (LIFO) stack using only two queues. The
implemented stack should support all the functions of a normal stack
(push, top, pop, and empty).

Notes:
* Use only standard queue operations (push to back, peek/pop from front,
  size, and is empty.)
* May use a list or double ended queue as long as only the above
  standard operations are used.
'''
class MyStack_two_queue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    '''
    Pushes element x to the top of the stack.
    '''
    # O(n) time
    def push(self, x: int) -> None:
        self.q1, self.q2 = self.q2, self.q1
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)

    '''
    Removes the element on the top of the stack and returns it.
    '''
    # O(1) time
    def pop(self) -> int:
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        return self.q1.popleft()

    '''
    Returns the element on the top of the stack.
    '''
    def top(self) -> int:
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        return self.q1[0]

    '''
    Returns true if the stack is empty false otherwise
    '''
    def empty(self) -> bool:
        return not self.q1 and not self.q2

class MyStack_one_queue:

    def __init__(self):
        self.q = deque()

    # O(n) time
    def push(self, x: int) -> None:
        n = len(self.q)
        self.q.append(x)
        for i in range(n):
            self.q.append(self.q.popleft())

    # O(1) time
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

class UnitTesting(unittest.TestCase):
    # The MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()

    def test_one(self):
        s = MyStack()
        self.assertEqual(s.empty(), True)
        s.push(1)
        self.assertEqual(s.empty(), False)
        self.assertEqual(s.top(), 1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.top(), 1)
        self.assertEqual(s.empty(), False)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.empty(), True)

    def test_two(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.top(), 5)
        self.assertEqual(s.pop(), 5)
        s.push(6)
        self.assertEqual(s.top(), 6)
        self.assertEqual(s.pop(), 6)
        s.push(7)
        self.assertEqual(s.top(), 7)
        self.assertEqual(s.pop(), 7)
        s.push(8)
        s.push(9)
        s.push(10)
        self.assertEqual(s.pop(), 10)
        self.assertEqual(s.pop(), 9)
        self.assertEqual(s.pop(), 8)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)