# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 1-indexed array of distinct integers nums of length n.

    Distribute all the elements of nums between two arrays arr1 and arr2 using n
    operations. In the first operation, append nums[1] to arr1. In the second
    operation, append nums[2] to arr2. Afterwards, in the ith operation:
    * If the last element of arr1 is greater than the last element of arr2,
      append nums[i] to arr1. Otherwise, append nums[i] to arr2.

    The array result is formed by concatenating the arrays arr1 and arr2.

    Return the array result.
    '''
    def resultArray(self, nums: List[int]) -> List[int]:
        a,b = [nums[0]], [nums[1]]
        for n in nums[2:]:
            if a[-1] > b[-1]:
                a.append(n)
            else:
                b.append(n)
        return a + b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3]
        o = [2,3,1]
        self.assertEqual(s.resultArray(i), o)

    def test_two(self):
        s = Solution()
        i = [5,4,3,8]
        o = [5,3,4,8]
        self.assertEqual(s.resultArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)