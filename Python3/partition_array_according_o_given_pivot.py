# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and an integer pivot. Rearrange nums
    such that the following conditions are satisfied:
    * Every element less than pivot appears before every element greater than
      pivot.
    * Every element equal to pivot appears in between the elements less than and
      greater than pivot.
    * The relative order of the elements less than pivot and the elements
      greater than pivot is maintained.
    
    return nums after the rearrangement.
    '''
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a,b,c = [], [], []
        for n in nums:
            if n < pivot:
                a.append(n)
            elif n == pivot:
                c.append(n)
            else:
                b.append(n)
        return a + c + b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [9,12,5,10,14,3,10]
        j = 10
        o = [9,5,3,10,10,12,14]
        self.assertEqual(s.pivotArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-3,4,3,2]
        j = 2
        o = [-3,2,4,3]
        self.assertEqual(s.pivotArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)