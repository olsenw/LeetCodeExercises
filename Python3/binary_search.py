# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums. If
    target exists then return its index. Otherwise return -1.

    The algorithm must have an O(log n) runtime complexity.
    '''
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        m = (i + j) // 2
        while i != j:
            if nums[m] < target:
                i = m + 1
            else:
                j = m
            m = (i + j) // 2
        return m if nums[i] == target else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,0,3,5,9,12]
        j = 9
        o = 4
        self.assertEqual(s.search(i, j), o)

    def test_two(self):
        s = Solution()
        i = [-1,0,3,5,9,12]
        j = 2
        o = -1
        self.assertEqual(s.search(i, j), o)

    def test_three(self):
        s = Solution()
        i = [-1,0,3,5,9]
        j = 9
        o = 4
        self.assertEqual(s.search(i, j), o)

    def test_four(self):
        s = Solution()
        i = [5]
        j = 5
        o = 0
        self.assertEqual(s.search(i, j), o)

    def test_five(self):
        s = Solution()
        i = [2,5]
        j = 5
        o = 1
        self.assertEqual(s.search(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)