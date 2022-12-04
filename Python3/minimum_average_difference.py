# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 0-indexed integer array nums of length n.

    The average difference of the index i is the absolute difference between the
    average of the first i + 1 elements of nums and the average of the last
    n - i - 1 elements. Both averages should be rounded down to the nearest
    integer.

    Return the index with the minimum average difference. If there are multiple
    such indices, return the smallest one.
    '''
    def minimumAverageDifference(self, nums: List[int]) -> int:
        answer = (10**5, 10**5)
        n = len(nums)
        r = sum(nums)
        l = 0
        for i in range(n-1):
            l += nums[i]
            r -= nums[i]
            answer = min(answer, (abs((l // (i + 1)) - (r // (n - i - 1))), i))
        return min(answer, ((l+nums[-1]) // n, n-1))[1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,3,9,5,3]
        o = 3
        self.assertEqual(s.minimumAverageDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [0]
        o = 0
        self.assertEqual(s.minimumAverageDifference(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1,1]
        o = 0
        self.assertEqual(s.minimumAverageDifference(i), o)

    def test_four(self):
        s = Solution()
        i = [4,2,0]
        o = 2
        self.assertEqual(s.minimumAverageDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)