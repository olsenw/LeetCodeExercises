# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing, decreasing = 0,0
        iCurr, dCurr = 1,1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                iCurr += 1
            else:
                increasing = max(increasing, iCurr)
                iCurr = 1
            if nums[i] < nums[i-1]:
                dCurr += 1
            else:
                decreasing = max(decreasing, dCurr)
                dCurr = 1
        return max(increasing, decreasing, iCurr, dCurr)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,3,3,2]
        o = 2
        self.assertEqual(s.longestMonotonicSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [3,3,3,3]
        o = 1
        self.assertEqual(s.longestMonotonicSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [3,2,1]
        o = 3
        self.assertEqual(s.longestMonotonicSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)