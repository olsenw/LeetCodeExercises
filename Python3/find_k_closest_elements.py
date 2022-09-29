# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from msvcrt import kbhit
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a sorted integer array arr, two integers k and x, return the k closest
    integers to x in the array. The result should also be sorted in ascending
    order.
    
    An integer a is closer to x than integer b if:
    * |a - x| < |b - x|
    * |a - x| == |b - x| and a < b'''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key=lambda a: (abs(a-x), a))[:k])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 4
        k = 3
        o = [1,2,3,4]
        self.assertEqual(s.findClosestElements(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 4
        k = -1
        o = [1,2,3,4]
        self.assertEqual(s.findClosestElements(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)