# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        answer = max(nums)
        # early return saves O(2n) calculations
        if answer < 0:
            return answer
        s = set(n for n in nums if n >= 0)
        if len(s) > 0:
            answer = max(answer, sum(s))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 15
        self.assertEqual(s.maxSum(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,0,1,1]
        o = 1
        self.assertEqual(s.maxSum(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,-1,-2,1,0,-1]
        o = 3
        self.assertEqual(s.maxSum(i), o)

    def test_four(self):
        s = Solution()
        i = [-3,-2,-1]
        o = -1
        self.assertEqual(s.maxSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)