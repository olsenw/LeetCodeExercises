# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue.

Note, only use standard operations of a stack.
'''
# O(n^2) time from forced moves to either stack
class MyQueue_slow:
    def __init__(self):
        self.a = []
        self.b = []
        
    '''
    Pushes element x to the back of the queue.
    '''
    def push(self, x: int) -> None:
        while self.b:
            self.a.append(self.b.pop())
        self.a.append(x)
        
    '''
    Removes the element from the front of the queue and returns it.
    '''
    def pop(self) -> int:
        while self.a:
            self.b.append(self.a.pop())
        return self.b.pop()
        
    '''
    Returns the element at the front of the queue.
    '''
    def peek(self) -> int:
        while self.a:
            self.b.append(self.a.pop())
        return self.b[-1]
        
    '''
    Returns true if the queue is empty, false otherwise.
    '''
    def empty(self) -> bool:
        return not self.a and not self.b

# O(n) only move to the peek/pop stack when have to
class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b.pop()

    def peek(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b[-1]
        
    def empty(self) -> bool:
        return not self.a and not self.b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = MyQueue()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.empty(), False)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.empty(), True)

if __name__ == '__main__':
    unittest.main(verbosity=2)