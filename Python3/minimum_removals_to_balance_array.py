# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k.

    An array is considered balanced if the value of its maximum element is at
    most k times the minimum element.

    It is possible to remove any number of elements from nums without making it
    empty.

    Return the minimum number of elements to remove so that the remaining array
    is balanced.

    Note: An array of size 1 is considered balanced as its maximum and minimum
    are equal, and the condition always holds true.
    '''
    # assumes removing values from right
    def minRemoval_partial(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = bisect.bisect(nums, nums[0] * k)
        return len(nums) - i

    def minRemoval(self, nums: List[int], k: int) -> int:
        answer = 0
        nums.sort()
        for i,n in enumerate(nums):
            j = bisect.bisect(nums, n * k)
            answer = max(answer, j - i)
        return len(nums) - answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,5]
        j = 2
        o = 1
        self.assertEqual(s.minRemoval(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,6,2,9]
        j = 3
        o = 2
        self.assertEqual(s.minRemoval(i,j), o)

    def test_three(self):
        s = Solution()
        i = [4,6]
        j = 2
        o = 0
        self.assertEqual(s.minRemoval(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,34,23]
        j = 2
        o = 1
        self.assertEqual(s.minRemoval(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)