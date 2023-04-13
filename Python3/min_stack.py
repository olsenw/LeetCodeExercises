# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.
'''
# had a moment of inspiration because of hint
class MinStack:
    # Initializes the stack object
    def __init__(self):
        self.s = []
        self.m = 2147483647
        
    # Pushes the element val onto the stack
    def push(self, val: int) -> None:
        self.m = min(self.m, val)
        self.s.append([val, self.m])
        
    # Removes the top element of the stack
    def pop(self) -> None:
        self.s.pop()
        if len(self.s):
            self.m = self.s[-1][1]
        else:
            self.m = 2147483647
        
    # Gets the top element of the stack
    def top(self) -> int:
        return self.s[-1][0]
        
    # retrieves the minimum element in the stack
    def getMin(self) -> int:
        return self.s[-1][1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = MinStack()
        s.push(-2)
        s.push(-0)
        s.push(-3)
        self.assertEqual(s.getMin(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), -2)

    def test_two(self):
        s = MinStack()
        s.push(2147483646)
        s.push(2147483646)
        s.push(2147483647)
        self.assertEqual(s.top(), 2147483647)
        s.pop()
        self.assertEqual(s.getMin(), 2147483646)
        s.pop()
        self.assertEqual(s.getMin(), 2147483646)
        s.pop()
        s.push(2147483647)
        self.assertEqual(s.top(), 2147483647)
        self.assertEqual(s.getMin(), 2147483647)
        s.push(-2147483648)
        self.assertEqual(s.top(), -2147483648)
        self.assertEqual(s.getMin(), -2147483648)
        s.pop()
        self.assertEqual(s.getMin(), 2147483647)

    def test_three(self):
        s = MinStack()
        s.push(-10)
        s.push(14)
        self.assertEqual(s.getMin(), -10)
        self.assertEqual(s.getMin(), -10)
        s.push(-20)
        self.assertEqual(s.getMin(), -20)
        self.assertEqual(s.getMin(), -20)
        self.assertEqual(s.top(), -20)
        self.assertEqual(s.getMin(), -20)
        s.pop()
        s.push(10)
        s.push(-7)
        self.assertEqual(s.getMin(), -10)
        s.push(-7)
        s.pop()
        self.assertEqual(s.top(), -7)
        self.assertEqual(s.getMin(), -10)
        s.pop()

if __name__ == '__main__':
    unittest.main(verbosity=2)