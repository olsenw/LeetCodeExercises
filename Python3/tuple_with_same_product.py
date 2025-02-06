# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of distinct positive integers, return the number of
    tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are
    elements of nums, and a != b != c != d.
    '''
    # hints help a lot
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums.sort()
        h = defaultdict(set)
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                i,j = nums[a], nums[b]
                h[i*j].add((i,j))
        answer = 0
        for i in h:
            n = len(h[i])
            if n < 2:
                continue
            answer += 4 * math.factorial(n) // math.factorial(n-2)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,4,6]
        o = 8
        self.assertEqual(s.tupleSameProduct(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,4,5,10]
        o = 16
        self.assertEqual(s.tupleSameProduct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)