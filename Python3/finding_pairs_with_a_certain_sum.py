# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Given two integer arrays nums1 and nums2. Implement a data structure that
supports two types of queries:
1) Add a positive integer to an element of a given index in the array nums2.
2) Count the number of pairs (i,j) such that nums1[i] + nums2[j] equals a
    given value (0 <= i < nums1.length and 0 <= j < nums2.length).

Implement the FindSUmPairs class:
'''
class FindSumPairs:
    '''
    Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
    '''
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = sorted(nums1)
        self.nums2 = nums2
        self.counter = Counter(nums2)

    '''
    Adds val to nums2[index], ie apply nums2[index] += val
    '''
    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter[self.nums2[index]] += 1
        return

    '''
    Returns the number of pairs (i,j) such that nums1[i] + nums2[j] == tot.
    '''
    def count(self, tot: int) -> int:
        answer = 0
        for i in self.nums1:
            answer += self.counter[tot - i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
        self.assertEqual(s.count(7), 8)
        s.add(3, 2)
        self.assertEqual(s.count(8), 2)
        self.assertEqual(s.count(4), 1)
        s.add(0, 1)
        s.add(1, 1)
        self.assertEqual(s.count(7), 11)

if __name__ == '__main__':
    unittest.main(verbosity=2)