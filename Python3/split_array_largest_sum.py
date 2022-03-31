# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import itertools
import functools

class Solution:
    '''
    Given an array nums which consists of non-negative integers and an
    integer m, which can be slit into m non-empty continuous subarrays.

    Write an algorithm to minimize the largest sum among these m
    subarrays.
    '''
    # based on binary search leetcode solution
    # https://leetcode.com/problems/split-array-largest-sum/solution/
    # O(N log S) time [N is length S is sum of array]
    # O(1) space
    def splitArray_binary(self, nums: List[int], m: int) -> int:
        # minimum possible largest sum (single element in array)
        i = max(nums)
        # largest possible sum
        j = sum(nums)
        # holds answer
        a = 0
        # binary search
        while i <= j:
            # mid point (guess at minimum largest sum)
            guess = (i + j) // 2
            # account how many segments needed for guess
            segments = 1
            # accumulator
            counter = 0
            for n in nums:
                # n fits in current segment
                if counter + n <= guess:
                    counter += n
                # start new segment
                else:
                    counter = n
                    segments += 1
            # lower right hand bound
            if segments <= m:
                j = guess - 1
                a = guess
            # increase left hand bound
            else:
                i = guess + 1
        # return answer
        return a

    # based on binary search leetcode solution
    # https://leetcode.com/problems/split-array-largest-sum/solution/
    # O(N^2 M) time [N is length M is segments]
    # O(N M) space
    def splitArray_dp_top(self, nums: List[int], m: int) -> int:
        n = len(nums)
        # precalc sums in array
        prefix = [0] + list(itertools.accumulate(nums))
        # cache subproblem answers
        @functools.lru_cache(None)
        # find best answer from index into remaining segments
        def sub_problem(i, c):
            # base case (sum remaining elements into last segment)
            if c == 1:
                return prefix[n] - prefix[i]
            # recurrence relation
            # excess of maximum sum segment could be
            minimum = prefix[n]
            # test all possible segments
            for j in range(i, n - c + 1):
                # sum of segment
                first = prefix[j + 1] - prefix[i]
                # find largest sum of subsegment
                large = max(first, sub_problem(j+1, c-1))
                # update minimum
                minimum = min(minimum, large)
                # early cutout
                if first >= minimum:
                    break
            return minimum
        return sub_problem(0, m)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [7,2,5,10,8]
        j = 2
        o = 18
        self.assertEqual(s.splitArray_binary(i, j), o)
        self.assertEqual(s.splitArray_dp_top(i, j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 2
        o = 9
        self.assertEqual(s.splitArray_binary(i, j), o)
        self.assertEqual(s.splitArray_dp_top(i, j), o)

    def test_three(self):
        s = Solution()
        i = [1,4,4]
        j = 3
        o = 4
        self.assertEqual(s.splitArray_binary(i, j), o)
        self.assertEqual(s.splitArray_dp_top(i, j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 1
        o = 15
        self.assertEqual(s.splitArray_binary(i, j), o)
        self.assertEqual(s.splitArray_dp_top(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)