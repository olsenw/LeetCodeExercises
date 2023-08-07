# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums with n objects colored red, white, or blue, sort them
    in-place so that the objects of the same color are adjacent, with the colors
    in the order red, white, blue.

    Use the integers 0, 1, and 2 to represents the colors red, white, and blue
    respectively.

    Solve this problem without using the library's sort function.
    '''
    def sortColors_brute(self, nums: List[int]) -> None:
        colors = [0] * 3
        for n in nums:
            colors[n] += 1
        i = 0
        for j in range(3):
            for _ in range(colors[j]):
                nums[i] = j
                i += 1

    # dutch national flag algorithm
    # https://leetcode.com/problems/sort-colors/solutions/3464652/beats-100-c-java-python-javascript-two-pointer-dutch-national-flag-algorithm/
    def sortColors(self, nums: List[int]) -> None:
        i,j,k = 0,0,len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j],nums[k] = nums[k], nums[j]
                k -= 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,0,2,1,1,0]
        s.sortColors(i)
        o = [0,0,1,1,2,2]
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [2,0,1]
        s.sortColors(i)
        o = [0,1,2]
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)