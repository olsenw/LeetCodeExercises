# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays arr1 and arr2, the elements of arr2 are distinct and all
    elements in arr2 are also in arr1.

    Sort the elements of arr1 such that the relative ordering of items in arr1
    are the same as in arr2. Elements that do not appear in arr2 should be
    placed at the end of arr1 in ascending order.
    '''
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        answer = []
        for i in arr2:
            answer += [i] * c[i]
            c[i] = 0
        answer += sorted(c.elements())
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,1,3,2,4,6,7,9,2,19]
        j = [2,1,4,3,9,6]
        o = [2,2,2,1,4,3,3,9,6,7,19]
        self.assertEqual(s.relativeSortArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [28,6,22,8,44,17]
        j = [22,28,8,6]
        o = [22,28,8,6,17,44]
        self.assertEqual(s.relativeSortArray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [4,3,2,1,1,1,1,2]
        j = [1,2,3,4]
        o = [1,1,1,1,2,2,3,4]
        self.assertEqual(s.relativeSortArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)