# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

'''
Design a number container system that can do the following
* Insert or Replace a number at the given index in the system.
* Return the smallest index for the given number in the system.

Implement the NumberContainers class:
'''
class NumberContainers:
    '''
    Initializes the number container system.
    '''
    def __init__(self):
        self.nums = defaultdict(SortedList)
        self.indices = dict()

    '''
    Fills the containers at index with the number. If there is already a number
    at that index, replace it.
    '''
    def change(self, index: int, number: int) -> None:
        if index in self.indices:
            n = self.indices[index]
            self.nums[n].remove(index)
            if len(self.nums[n]) == 0:
                del self.nums[n]
        self.indices[index] = number
        self.nums[number].add(index)

    '''
    Returns the smallest index for the given number, or -1 if there is no index
    that is filled by number in the system.
    '''
    def find(self, number: int) -> int:
        return self.nums[number][0] if number in self.nums else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = NumberContainers()
        self.assertEqual(s.find(10), -1)
        s.change(2, 10)
        s.change(1, 10)
        s.change(3, 10)
        s.change(5, 10)
        self.assertEqual(s.find(10), 1)
        s.change(1, 20)
        self.assertEqual(s.find(10), 2)
    
    def test_two(self):
        s = NumberContainers()
        s.change(1, 10)
        self.assertEqual(s.find(10), 1)
        s.change(1, 20)
        self.assertEqual(s.find(10), -1)
        self.assertEqual(s.find(20), 1)
        self.assertEqual(s.find(30), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)