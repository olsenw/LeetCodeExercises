# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three positive integers: n, index, and maxSum. Construct an array nums
    (0-indexed) that satisfies the following conditions:
    * nums.length == n
    * nums[i] is a positive integer where 0 <= i < n
    * abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n - 1
    * The sum of all the elements of nums does not exceed maxSum
    * nums[index] is maximized

    Return nums[index] of the constructed array.

    Note that abs(x) equals x if x >= 0, and -x otherwise.
    '''
    # based on editorial from LeetCode
    # https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/editorial/
    # had the right idea about binary search for value
    # was unsure on how to calculate the value of resulting array
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def s(value):
            count = 0
            # index left
            if value > index:
                count += (value + value - index) * (index + 1) // 2
            else:
                count += (value + 1) * value // 2 + index - value + 1
            # index right
            if value >= n - index:
                count += (value + value - n + 1 + index) * (n - index) // 2
            else:
                count += (value + 1) * value // 2 + n - index - value
            return count - value
        i, j = 1, maxSum
        while i < j:
            k = (i + j + 1) // 2
            if s(k) <= maxSum:
                i = k
            else:
                j = k - 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 2
        k = 6
        o = 2
        self.assertEqual(s.maxValue(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = 1
        k = 10
        o = 3
        self.assertEqual(s.maxValue(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)