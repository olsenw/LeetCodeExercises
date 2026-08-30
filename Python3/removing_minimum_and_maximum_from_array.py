# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of distinct integers nums.

    There is an element in nums that has the lowest value and an element that
    has the highest value. They are called the minimum and maximum respectively.
    Remove both of these elements from the array.

    A deletion is defined as either removing an element from the front of the
    array or removing an element from the back of the array.

    Return the minimum number of deletions it would take to remove both the
    minimum and maximum elements from the array.
    '''
    def minimumDeletions(self, nums: List[int]) -> int:
        # if len(nums) < 3:
        #     return len(nums)
        n = len(nums)
        # minimum, maximum
        a,b = float('inf'),float('-inf')
        x,y = -1,-1
        for i,j in enumerate(nums):
            if j < a:
                a = j
                x = i
            if j > b:
                b = j
                y = i
        # only remove from the left
        i = max(x,y) + 1
        # remove from left and right
        j = (min(x,y) + 1) + (n - max(x,y))
        # only remove from the right
        k = n - min(x,y)
        return min(i,j,k)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,10,7,5,4,1,8,6]
        o = 5
        self.assertEqual(s.minimumDeletions(i), o)

    def test_two(self):
        s = Solution()
        i = [0,-4,19,1,8,-2,-3,5]
        o = 3
        self.assertEqual(s.minimumDeletions(i), o)

    def test_three(self):
        s = Solution()
        i = [101]
        o = 1
        self.assertEqual(s.minimumDeletions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)