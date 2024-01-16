# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n, create an array ans of length 2n
    where ans[i] == nums[i] and ans[i+n] == nums[i] for 0 <= i < n (0-indexed).

    Specifically, ans is the concatenation of two nums arrays.

    Return the array ans.
    '''
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1]
        o = [1,2,1,1,2,1]
        self.assertEqual(s.getConcatenation(i), o)

    def test_two(self):
        s = Solution()
        i = [1,3,2,1]
        o = [1,3,2,1,1,3,2,1]
        self.assertEqual(s.getConcatenation(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)