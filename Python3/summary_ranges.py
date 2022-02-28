# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a sorted unique integer array nums.

    Return the smallest sorted list of ranges that cover all the numbers
    in the array exactly. That is each element of nums is covered by
    exactly one of the ranges, and there is no integer x such that x is
    in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:
    * "a->b" if a != b
    * "a" if a == b
    '''
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []
        ranges = []
        l, r = nums[0], nums[0]
        for n in nums[1:]:
            # new range starts
            if r+1 < n:
                ranges.append(f"{l}->{r}" if l < r else f"{l}")
                l, r = n, n
            # extend old range
            else:
                r = n
        ranges.append(f"{l}->{r}" if l < r else f"{l}")
        return ranges

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,2,4,5,7]
        o = ["0->2", "4->5", "7"]
        self.assertEqual(s.summaryRanges(i), o)

    def test_two(self):
        s = Solution()
        i = [0,2,3,4,6,8,9]
        o = ["0", "2->4", "6", "8->9"]
        self.assertEqual(s.summaryRanges(i), o)

    def test_three(self):
        s = Solution()
        i = []
        o = []
        self.assertEqual(s.summaryRanges(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)