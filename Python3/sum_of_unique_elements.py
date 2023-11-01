# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. The unique elements of an array are the
    elements that appear exactly once in the array.

    Return the sum of all the unique elements of nums.
    '''
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum(i for i in c if c[i] == 1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,2]
        o = 4
        self.assertEqual(s.sumOfUnique(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1,1]
        o = 0
        self.assertEqual(s.sumOfUnique(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 15
        self.assertEqual(s.sumOfUnique(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)