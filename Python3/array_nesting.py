# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n where nums is a permutation of the
    numbers in the range [0, n - 1].

    Build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ...}
    subjected to the following rules:
    * The first element in s[k] starts with the selection of the element nums[k]
      of index = k.
    * The next elements in s[k] should be nums[nums[k]], and then
      nums[nums[nums[k]]], and so on.
    * Stop adding right before a duplicate element occurs in s[k].
    
    Return the longest length of a set s[k].
    '''
    def arrayNesting(self, nums: List[int]) -> int:
        v = set()
        @cache
        def dfs(k:int):
            if nums[k] in v:
                return 0
            v.add(nums[k])
            a = dfs(nums[k])
            v.remove(nums[k])
            return 1 + a
        return max(dfs(k) for k in nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,4,0,3,1,6,2]
        o = 4
        self.assertEqual(s.arrayNesting(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,2]
        o = 1
        self.assertEqual(s.arrayNesting(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)