# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a sorted array of distinct integers and a target value, return the
    index if the target is found. If not, return the index where it would be if
    it were inserted in order.

    Write an algorithm with O(log(n)) runtime complexity.
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0, len(nums)
        while i < j:
            k = (j - i) // 2 + i
            if target > nums[k]:
                i = k + 1
            else:
                j = k
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,6]
        j = 5
        o = 2
        self.assertEqual(s.searchInsert(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,3,5,6]
        j = 2
        o = 1
        self.assertEqual(s.searchInsert(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,3,5,6]
        j = 7
        o = 4
        self.assertEqual(s.searchInsert(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)