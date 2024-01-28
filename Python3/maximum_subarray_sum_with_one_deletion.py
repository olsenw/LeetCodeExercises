# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers, return the maximum sum for a non-empty subarray
    (contiguous elements) with at most one element deletion. In other words,
    choose a subarray and optionally delete one element such that there is still
    at least one element left and the sum of the remaining elements is the
    maximum possible.

    Note that the subarray needs to be non-empty after deleting one element.
    '''
    # based on solution by Cubicon
    # https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/solutions/377373/python-solution-with-explanation-using-2-variables-o-n-time-o-1-space/
    def maximumSum(self, arr: List[int]) -> int:
        # running sum skipping any given index
        skip = 0
        # running sum without skipping any element
        notskip = 0
        answer = max(arr)
        for n in arr:
            # no point to skip positive integer (only increase maximum)
            if n >= 0:
                skip += n
            # if skipping this value is a better maximum than a previous number
            else:
                skip = max(skip + n, notskip)
            notskip += n
            answer = max(answer, skip if skip != 0 else -math.inf, notskip if notskip != 0 else -math.inf)
            # restart sum of subarray (previous subarray is negative)
            if skip < 0: skip = 0
            if notskip < 0: notskip = 0
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,-2,0,3]
        o = 4
        self.assertEqual(s.maximumSum(i), o)

    def test_two(self):
        s = Solution()
        i = [1,-2,-2,3]
        o = 3
        self.assertEqual(s.maximumSum(i), o)

    def test_three(self):
        s = Solution()
        i = [-1,-1,-1,-1]
        o = -1
        self.assertEqual(s.maximumSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)