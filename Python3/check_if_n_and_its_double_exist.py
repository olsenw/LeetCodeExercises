# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array arr of integers, check if there exist two indices i and j
    such that:
    * i != j
    * 0 <= i, j < arr.length
    * arr[i] == 2 * arr[j]
    '''
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for a in arr:
            if 2 * a in s or (a % 2 == 0 and a // 2 in s):
                return True
            s.add(a)
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,2,5,3]
        o = True
        self.assertEqual(s.checkIfExist(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,7,11]
        o = False
        self.assertEqual(s.checkIfExist(i), o)

    def test_three(self):
        s = Solution()
        i = [1,0]
        o = False
        self.assertEqual(s.checkIfExist(i), o)

    def test_four(self):
        s = Solution()
        i = [0,0]
        o = True
        self.assertEqual(s.checkIfExist(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)