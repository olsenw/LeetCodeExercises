# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three integer arrays nums1, nums2, and nums3, return a distinct array
    containing all the values that are present in at least two out of the three
    arrays. The values may be returned in any order.
    '''
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c = Counter()
        for i in set(nums1):
            c[i] += 1
        for i in set(nums2):
            c[i] += 1
        for i in set(nums3):
            c[i] += 1
        return [i for i in c if c[i] > 1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,3,2]
        j = [2,3]
        k = [3]
        o = [3,2]
        self.assertEqual(s.twoOutOfThree(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [3,1]
        j = [2,3]
        k = [1,2]
        o = [2,3,1]
        self.assertEqual(s.twoOutOfThree(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2,2]
        j = [4,3,3]
        k = [5]
        o = []
        self.assertEqual(s.twoOutOfThree(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)