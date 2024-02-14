# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of even length consisting of an equal
    number of positive and negative integers.

    Rearrange the elements of nums such that the modified array follows the
    given conditions:
    1) Every consecutive pair of integers have opposite signs.
    2) For all integers with the same sign, the order in which they were present
       in nums is preserved
    3) The rearranged array begins with a positive integer.

    Return the modified array after rearranging the elements to satisfy the
    aforementioned conditions.
    '''
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [n for n in nums if n > 0]
        b = [n for n in nums if n < 0]
        for i,(j,k) in enumerate(zip(a,b)):
            nums[2 * i] = j
            nums[2 * i + 1] = k
        return nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,-2,-5,2,-4]
        o = [3,-2,1,-5,2,-4]
        self.assertEqual(s.rearrangeArray(i), o)

    def test_two(self):
        s = Solution()
        i = [-1,1]
        o = [1,-1]
        self.assertEqual(s.rearrangeArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)