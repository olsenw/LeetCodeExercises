# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        s = 0
        for g in gain:
            s += g
            a = max(a, s)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-5,1,5,0,-7]
        o = 1
        self.assertEqual(s.largestAltitude(i), o)

    def test_two(self):
        s = Solution()
        i = [-4,-3,-2,-1,4,3,2]
        o = 0
        self.assertEqual(s.largestAltitude(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)