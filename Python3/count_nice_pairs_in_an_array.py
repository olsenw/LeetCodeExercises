# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums that consists of non-negative integers. Let rev(x) be
    defined as the revers of the non-negative integer x. For example,
    rev(123) = 321, and rev(120) = 21. A pair of indices (i,j) is nice if it
    satisfies all of the following conditions:
    * 0 <= i < j < nums.length
    * nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

    Return the number of nice pairs of indices. Since that number can be too
    large, return it modulo 10^9 + 7.
    '''
    # hints are very helpful
    def countNicePairs(self, nums: List[int]) -> int:
        answer = 0
        rev = [n - int(str(n)[::-1]) for n in nums]
        c = Counter()
        for r in rev:
            answer += c[r]
            c[r] += 1
        return answer % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [42,11,1,97]
        o = 2
        self.assertEqual(s.countNicePairs(i), o)

    def test_two(self):
        s = Solution()
        i = [13,10,35,24,76]
        o = 4
        self.assertEqual(s.countNicePairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)