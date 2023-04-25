# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Given a set which contains all positive integers [1,2,3,4,5,...].

Implement the SmallestInfiniteSet class:
'''
class SmallestInfiniteSet:
    '''
    Initializes the SmallestInfiniteSet object to contain all positive integers.
    '''
    def __init__(self):
        self.h = [] # min heap
        self.s = set() # set to prevent duplicates
        self.i = 1
        
    '''
    Removes and returns the smallest integer contained in the infinite set.
    '''
    def popSmallest(self) -> int:
        if self.h:
            self.s.remove(self.h[0])
            return heapq.heappop(self.h)
        self.i += 1
        return self.i - 1
        
    '''
    Adds a positive integer num back into the infinite set, if it is not already
    in the infinite set.
    '''
    def addBack(self, num: int) -> None:
        if num < self.i and num not in self.s:
            self.s.add(num)
            heapq.heappush(self.h, num)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = SmallestInfiniteSet()
        s.addBack(2)
        self.assertEqual(s.popSmallest(), 1)
        self.assertEqual(s.popSmallest(), 2)
        self.assertEqual(s.popSmallest(), 3)
        s.addBack(1)
        self.assertEqual(s.popSmallest(), 1)
        self.assertEqual(s.popSmallest(), 4)
        self.assertEqual(s.popSmallest(), 5)

    # def test_two(self):
    #     s = SmallestInfiniteSet()
    #     i = [1,2,3,4,5]
    #     o = 5
    #     self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)