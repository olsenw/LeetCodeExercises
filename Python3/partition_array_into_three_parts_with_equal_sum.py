# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr, return true if the array can be partitioned
    into three non-empty parts with equals sums.
    '''
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr) - arr[0]
        a = arr[0]
        d = {arr[0]:0}
        for i in range(1,len(arr)-1):
            s -= arr[i]
            a += arr[i]
            if s * 2 == a and s in d:
                return True
            d[a] = i
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,2,1,-6,6,-7,9,1,2,0,1]
        o = True
        self.assertEqual(s.canThreePartsEqualSum(i), o)

    def test_two(self):
        s = Solution()
        i = [0,2,1,-6,6,7,9,-1,2,0,1]
        o = False
        self.assertEqual(s.canThreePartsEqualSum(i), o)

    def test_three(self):
        s = Solution()
        i = [3,3,6,5,-2,2,5,1,-9,4]
        o = True
        self.assertEqual(s.canThreePartsEqualSum(i), o)

    def test_four(self):
        s = Solution()
        i = [1,-1,1,-1]
        o = False
        self.assertEqual(s.canThreePartsEqualSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)