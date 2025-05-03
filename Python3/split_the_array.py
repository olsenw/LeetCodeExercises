# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of even length. Split the array into two parts
    nums1 and nums2 such that:
    * nums1.length == num2.length == nums.length / 2
    * nums1 should contain distinct elements.
    * nums2 should contain distinct elements.

    Return true if it is possible to split the array, and false otherwise.
    '''
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums) % 2:
            return False
        c = Counter(nums)
        a,b = 0,0
        for i in c:
            if c[i] > 2:
                return False
            elif c[i] == 1:
                if a <= b:
                    a += 1
                else:
                    b += 1
        return a == b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,3,4]
        o = True
        self.assertEqual(s.isPossibleToSplit(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1]
        o = False
        self.assertEqual(s.isPossibleToSplit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)