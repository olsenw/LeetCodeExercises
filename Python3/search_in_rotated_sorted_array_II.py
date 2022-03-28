# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is an integer array nums sorted in non-decreasing order (may
    contain duplicate values).

    Before the array is passed into the function, it is rotated at an
    unknown pivot index k (0 <= k <= nums length) such that the 
    resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0],
    nums[1], ..., nums[k-1]].

    Given the rotated array and a target value, return true if target is
    in nums, or false otherwise.

    Attempt to decrease number of operations as much as possible.
    '''
    # based on leetcode solution (pictures help explain)
    # https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution/
    # O(n) worst case O(log n) best case
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        j = len(nums) - 1
        while i <= j:
            # midpoint in current search area
            m = (i + j) // 2
            # find target ?
            if nums[m] == target:
                return True
            # duplicates obfuscating pivot (linear search)
            if nums[i] == nums[m]:
                i += 1
                continue
            # binary search
            # is pivot left/right of midpoint
            p = nums[i] <= nums[m]
            # is target possibly in left half of pivot
            t = nums[i] <= target
            # pivot and target are oppsite sides of array
            if p ^ t:
                # pivot is left while target is right
                if p:
                    i = m + 1
                # target is left while pivot is right
                else:
                    j = m - 1
            # pivot and target same half of array
            else:
                if nums[m] < target:
                    i = m + 1
                else:
                    j = m - 1
        # did not find
        return False

    def search_linear(self, nums: List[int], target: int) -> bool:
        return target in nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,6,0,0,1,2]
        j = 0
        o = True
        self.assertEqual(s.search(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,5,6,0,0,1,2]
        j = 3
        o = False
        self.assertEqual(s.search(i,j), o)

    def test_three(self):
        s = Solution()
        i = [4,5,6,0,0,1,2]
        j = 4
        o = True
        self.assertEqual(s.search(i,j), o)

    def test_four(self):
        s = Solution()
        i = [4,5,6,7,8,0,1,2]
        j = 4
        o = True
        self.assertEqual(s.search(i,j), o)

    def test_five(self):
        s = Solution()
        i = [4,5,6,7,8,0,1,2]
        j = 9
        o = False
        self.assertEqual(s.search(i,j), o)

    def test_six(self):
        s = Solution()
        i = [1,0,1,1,1]
        j = 0
        o = True
        self.assertEqual(s.search(i,j), o)

    def test_seven(self):
        s = Solution()
        i = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
        j = 2
        o = True
        self.assertEqual(s.search(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)