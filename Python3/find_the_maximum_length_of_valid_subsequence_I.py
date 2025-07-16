# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    A subsequence sub of nums with length x is called valid if it satisfies:
    * (sub[0]+sub[1])%2 == (sub[1]+sub[2])%2 == ... == (sub[x-2]+sub[x-1])%2

    Return the length of the longest valid subsequence of nums.

    A subsequence is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.
    '''
    def maximumLength(self, nums: List[int]) -> int:
        even = sum(n % 2 == 0 for n in nums)
        last = not (nums[0] % 2)
        answer = 0
        for n in nums:
            if n % 2 != last:
                last = not last
                answer += 1
        return max(answer, even, len(nums) - even)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = 4
        self.assertEqual(s.maximumLength(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1,1,2,1,2]
        o = 6
        self.assertEqual(s.maximumLength(i), o)

    def test_three(self):
        s = Solution()
        i = [1,3]
        o = 2
        self.assertEqual(s.maximumLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)