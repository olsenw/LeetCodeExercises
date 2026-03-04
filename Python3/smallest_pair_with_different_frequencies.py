# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Consider all pairs of distinct values x and y from nums such that:
    * x < y
    * x and y have different frequencies in nums.

    Among all such pairs:
    * Choose the pair with the smallest possible value of x.
    * If multiple pairs have the same x, choose the one with the smallest
      possible value of y.

    Return an integer array [x, y]. If no valid pair exists return [-1,-1].
    '''
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        keys = sorted(c.keys())
        n = len(keys)
        for i in range(n):
            a = keys[i]
            for j in range(i+1,n):
                b = keys[j]
                if c[a] != c[b]:
                    return [a,b]
        return [-1,-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,3,4]
        o = [1,3]
        self.assertEqual(s.minDistinctFreqPair(i), o)

    def test_two(self):
        s = Solution()
        i = [1,5]
        o = [-1,-1]
        self.assertEqual(s.minDistinctFreqPair(i), o)

    def test_three(self):
        s = Solution()
        i = [7]
        o = [-1,-1]
        self.assertEqual(s.minDistinctFreqPair(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)