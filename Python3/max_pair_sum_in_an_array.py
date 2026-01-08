# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. Find the maximum sum of a pair of numbers from
    nums such that the largest digit in both numbers is equal.

    Return the maximum sum or -1 if no such pair exists.
    '''
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for n in nums:
            d[max(str(n))].append(n)
        answer=-1
        for i in d:
            for j in range(len(d[i])):
                for k in range(j+1, len(d[i])):
                    answer = max(answer, d[i][j] + d[i][k])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [112,131,411]
        o = -1
        self.assertEqual(s.maxSum(i), o)

    def test_two(self):
        s = Solution()
        i = [2536,1613,3366,162]
        o = 5902
        self.assertEqual(s.maxSum(i), o)

    def test_three(self):
        s = Solution()
        i = [51,71,17,24,42]
        o = 88
        self.assertEqual(s.maxSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)