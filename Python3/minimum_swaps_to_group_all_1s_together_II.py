# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A swap is defined as taking two distinct positions in an array and swapping
    the values in them.

    A circular array is defined as an array where the first element and the last
    element are considered to be adjacent.

    Given a binary circular array nums, return the minimum number of swaps
    required to group all 1's present in the array together at any location.
    '''
    # does not account for moving a distant one into a zero spot
    def minSwaps_wrong(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones <= 1:
            return 0
        nums = nums + nums
        i,k = 0, nums[0]
        answer = len(nums)
        for j in range(1, len(nums)):
            k += nums[j]
            pass
            while k == ones:
                answer = min(answer, j - i + 1)
                k -= nums[i]
                i += 1
        return answer - ones

    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        nums = nums + nums
        i = 0
        k = nums[i:ones].count(1)
        answer = ones - k
        for j in range(ones, len(nums)):
            k += nums[j]
            k -= nums[i]
            i += 1
            answer = min(answer, ones - k)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,0,1,1,0,0]
        o = 1
        self.assertEqual(s.minSwaps(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,1,1,0,0,1,1,0]
        o = 2
        self.assertEqual(s.minSwaps(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,0,0,1]
        o = 0
        self.assertEqual(s.minSwaps(i), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1,0,0,1,0,1,1,0]
        o = 1
        self.assertEqual(s.minSwaps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)