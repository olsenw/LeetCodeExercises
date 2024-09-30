# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:
'''
class CustomStack:
    '''
    Initializes the object with maxSize which is the maximum number of elements
    in the stack.
    '''
    def __init__(self, maxSize: int):
        self.limit = maxSize
        self.stack = []
        self.add = []
        return

    '''
    Adds x to the top of the stack if the stack has not reached the maxSize.
    '''
    def push(self, x: int) -> None:
        if len(self.stack) < self.limit:
            self.stack.append(x)
            self.add.append(0)

    '''
    Pops and returns the top of the stack or -1 if the stack is empty.
    '''
    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        b = self.add.pop()
        if self.add:
            self.add[-1] += b
        return self.stack.pop() + b

    '''
    Increments the bottom k elements of the stack by val. If there are less than
    k elements in the stack, increment all the elements in the stack.
    '''
    def increment(self, k: int, val: int) -> None:
        if len(self.add) == 0:
            return
        if k > len(self.add):
            self.add[-1] += val
        else:
            self.add[k - 1] += val

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = CustomStack(3)
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        s.push(2)
        s.push(3)
        s.push(4)
        s.increment(5,100)
        s.increment(2,100)
        self.assertEqual(s.pop(), 103)
        self.assertEqual(s.pop(), 202)
        self.assertEqual(s.pop(), 201)
        self.assertEqual(s.pop(), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)