# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array arr. Sort the integers in the array in ascending
    order by the number of 1's in their binary representation and in case of two
    of more integers have the same number of 1's, sort them in ascending order.

    Return the array after sorting it.
    '''
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(),x))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,2,3,4,5,6,7,8]
        o = [0,1,2,4,8,3,5,6,7]
        self.assertEqual(s.sortByBits(i), o)

    def test_two(self):
        s = Solution()
        i = [1024,512,256,128,64,32,16,8,4,2,1]
        o = [1,2,4,8,16,32,64,128,256,512,1024]
        self.assertEqual(s.sortByBits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)