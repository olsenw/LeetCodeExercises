# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import random
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Implement the RandomizedSet class.

Implement the functions of the class such that each function has an average O(1)
time complexity.
'''
class RandomizedSet:
    '''
    Initializes the RandomizedSet object.
    '''
    def __init__(self):
        self.stack = []
        self.dict = dict()

    '''
    Inserts an item val into the set if not present. Returns true if the item
    was not present, false otherwise.
    '''
    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.stack)
            self.stack.append(val)
            return True
        return False

    '''
    Removes an item val from the set if present. Returns true if the item was
    present, false otherwise.
    '''
    def remove(self, val: int) -> bool:
        if val in self.dict:
            i = self.dict[val]
            v = self.stack[-1]
            self.stack[i] = v
            self.dict[v] = i
            del self.dict[val]
            self.stack.pop()
            return True
        return False

    '''
    Returns a random element from the current set of elements (it's guaranteed
    that at least one element exists when this method is called). Each element
    must have the same probability of being returned.
    '''
    def getRandom(self) -> int:
        return self.stack[random.randint(0, len(self.stack)-1)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = RandomizedSet()
        self.assertEqual(s.insert(1), True)
        self.assertEqual(s.remove(2), False)
        self.assertEqual(s.insert(2), True)
        # random check
        self.assertEqual(s.remove(1), True)
        self.assertEqual(s.insert(2), False)
        # random with single element

    def test_two(self):
        s = RandomizedSet()
        self.assertEqual(s.remove(0), False)
        self.assertEqual(s.remove(0), False)
        self.assertEqual(s.insert(0), True)
        # random
        self.assertEqual(s.remove(0), True)
        self.assertEqual(s.insert(0), True)

    def test_three(self):
        s = RandomizedSet()
        self.assertEqual(s.insert(-1), True)
        self.assertEqual(s.remove(-2), False)
        self.assertEqual(s.insert(-2), True)
        # random
        self.assertEqual(s.remove(-1), True)
        self.assertEqual(s.insert(-2), False)
        # random

    def test_four(self):
        s = RandomizedSet()
        self.assertEqual(s.insert(0), True)
        self.assertEqual(s.insert(1), True)
        self.assertEqual(s.remove(0), True)
        self.assertEqual(s.insert(2), True)
        self.assertEqual(s.remove(1), True)
        # random

if __name__ == '__main__':
    unittest.main(verbosity=2)