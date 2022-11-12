# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from sortedcontainers import SortedList
import heapq

'''
The median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value, and the median is the mean of the two
middle values.

Examples
* [2,3,4] has a median of 3
* [2,3] has a median of (2+3)/2 = 2.5

Implement the MedianFinder class.
'''
# passes (probably due to how well SortedList is implemented)
class MedianFinder_SortedList:
    '''Initializes the MedianFinder object.'''
    def __init__(self):
        self.l = SortedList()

    '''Adds the integer num from the data stream to the data structure'''
    def addNum(self, num: int) -> None:
        self.l.add(num)

    '''Returns the median of all elements so far'''
    # must be within 10^-5 of the actual answer
    def findMedian(self) -> float:
        n = len(self.l)
        if n % 2:
            return self.l[n // 2]
        else:
            return (self.l[(n - 1) // 2] + self.l[n // 2]) / 2

# from leetcode 1387ms submission
# https://leetcode.com/submissions/api/detail/295/python3/1387/
class MedianFinder_Heapq:
    def __init__(self):
        self.hmn_hp = []  # the larger half of the list, min heap
        self.lmx_hp = []  # the smaller half of the list, max heap (invert min-heap)

    def addNum(self, num):
        if len(self.lmx_hp) == len(self.hmn_hp):
            heappush(self.hmn_hp, -heappushpop(self.lmx_hp, -num))
        else:
            heappush(self.lmx_hp, -heappushpop(self.hmn_hp, num))

    def findMedian(self): # min/max is the first one the heap list
        if len(self.lmx_hp) == len(self.hmn_hp):
            return float(-self.lmx_hp[0] + self.hmn_hp[0]) / 2.0
        else:
            return float(self.hmn_hp[0]) # high min heap with one more element, the smallest one is what we look for

class UnitTesting(unittest.TestCase):
    def test_one(self):
        m = MedianFinder()
        m.addNum(1)
        m.addNum(2)
        self.assertAlmostEqual(m.findMedian(), 1.5, 6)
        m.addNum(3)
        self.assertAlmostEqual(m.findMedian(), 2.0, 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)