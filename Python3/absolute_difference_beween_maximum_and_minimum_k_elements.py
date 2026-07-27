# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k.

    Find the absolute difference between:
    * the sum of the k largest elements in the array
    * the sum of the k smallest elements in the array

    Return an integer denoting the difference.
    '''
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        a = sum(nums[:k])
        b = sum(nums[-k:])
        return abs(a - b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,2,4]
        j = 2
        o = 5
        self.assertEqual(s.absDifference(i,j), o)

    def test_two(self):
        s = Solution()
        i = [100]
        j = 1
        o = 0
        self.assertEqual(s.absDifference(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)