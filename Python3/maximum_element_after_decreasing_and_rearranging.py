# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers arr. Perform some operations (possibly
    none) on arr so that it satisfies these conditions:
    * The value of the first element in arr must be 1.
    * The absolute difference between any 2 adjacent elements must be less than
      or equal to 1.

    There are 2 types of operations that can be performed any number of times:
    * Decrease the value of any element of arr to a smaller positive integer.
    * Rearrange the elements of arr to be in any order.

    Return the maximum possible value of an element in arr after performing the
    operations to satisfy the conditions.
    '''
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1,len(arr)):
            arr[i] = min(arr[i-1] + 1, arr[i])
        return arr[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,1,2,1]
        o = 2
        self.assertEqual(s.maximumElementAfterDecrementingAndRearranging(i), o)

    def test_two(self):
        s = Solution()
        i = [100,1,1000]
        o = 3
        self.assertEqual(s.maximumElementAfterDecrementingAndRearranging(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.maximumElementAfterDecrementingAndRearranging(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)