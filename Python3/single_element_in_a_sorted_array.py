# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a sorted array consisting of only integers where every element appears
    exactly twice, except for one element which appears exactly once.

    Return the single element that appears only once.

    The solution must run in O(log n) time and O(1) space.
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        k = (len(nums) - 1) // 2
        # index is odd
        if k % 2:
            if nums[k] == nums[k-1]:
                return self.singleNonDuplicate(nums[k+1:])
            else:
                return self.singleNonDuplicate(nums[:k])
        # index is even
        else:
            if nums[k] == nums[k+1]:
                return self.singleNonDuplicate(nums[k+2:])
            else:
                return self.singleNonDuplicate(nums[:k+1])

class UnitTesting(unittest.TestCase):
    '''
     0 1 2 3 4 5 6 7 8
     >   |   <       <
    [1,1,2,3,3,4,4,8,8]
    '''
    def test_one(self):
        s = Solution()
        i = [1,1,2,3,3,4,4,8,8]
        o = 2
        self.assertEqual(s.singleNonDuplicate(i), o)

    '''
     0 1 2 3 4  5  6
     >     > |     <
    [3,3,7,7,10,11,11]
    '''
    def test_two(self):
        s = Solution()
        i = [3,3,7,7,10,11,11]
        o = 10
        self.assertEqual(s.singleNonDuplicate(i), o)

    '''
     0 1 2 3 4 5 6
                 |
    [1,1,2,2,3,3,4]
    '''
    def test_three(self):
        s = Solution()
        i = [1,1,2,2,3,3,4]
        o = 4
        self.assertEqual(s.singleNonDuplicate(i), o)

    '''
     0 1 2 3 4 5 6
     |
    [1,2,2,3,3,4,4]
    '''
    def test_four(self):
        s = Solution()
        i = [1,2,2,3,3,4,4]
        o = 1
        self.assertEqual(s.singleNonDuplicate(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)