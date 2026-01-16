# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1)
    and (m, n) containing some horizontal and vertical fences given in arrays 
    hFences and vFences respectively.

    Horizontal fences are from the coordinates (hFences[i], i) to
    (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i])
    to (m, vFences[i]).

    Return the maximum area of a square field that can be formed by removing
    some fences (possibly none) or -1 if it is impossible to make a square
    field.

    Since the answer may be large, return it modulo 10^9 + 7.

    Note: The field is surrounded by two horizontal fences from the coordinates
    (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the
    coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be
    removed.
    '''
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        modulo = 10**9 + 7
        hFences.append(1)
        hFences.append(m)
        hFences.sort()
        horizontal = set()
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                horizontal.add(hFences[j] - hFences[i])
        vFences.append(1)
        vFences.append(n)
        vFences.sort()
        vertical = set()
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                vertical.add(vFences[j] - vFences[i])
        intersect = horizontal.intersection(vertical)
        if len(intersect) == 0:
            return -1
        answer = max(intersect)
        return (answer * answer) % modulo

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 3
        k = [2,3]
        l = [2]
        o = 4
        self.assertEqual(s.maximizeSquareArea(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = 7
        k = [2]
        l = [4]
        o = -1
        self.assertEqual(s.maximizeSquareArea(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)