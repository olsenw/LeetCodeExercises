# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 1-dimensional (1D) integer array original, and two
    integers, m and n. Create a 2-dimensional (2D) array with m rows and n
    columns using all the elements from original.

    The elements from indices 0 to n - 1 (inclusive) of original should form the
    first row of the constructed 2D array, the elements from n to 2 * n - 1
    (inclusive) should form the the second row of the constructed 2D array, and
    so on.

    Return an m x n 2D array constructed according to the above procedure, or an
    empty 2D array if it is impossible.
    '''
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n == len(original):
            return [[original[j] for j in range((i-1) * n, i * n)] for i in range(1,m+1)]
        else:
            return []

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = 2
        k = 2
        o = [[1,2],[3,4]]
        self.assertEqual(s.construct2DArray(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        j = 1
        k = 3
        o = [[1,2,3]]
        self.assertEqual(s.construct2DArray(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2]
        j = 1
        k = 1
        o = []
        self.assertEqual(s.construct2DArray(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)