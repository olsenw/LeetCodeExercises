# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a special square room with mirrors on each of the four
    walls. Except for the southwest corner, there are receptors on each
    of the remaining corners, numbered 0, 1, and 2.

    The square room has walls of length p and a laser ray from the
    southwest corner first meets the east wall at a distance q from the
    0th receptor.

    Given the two integers p and q, return the number of receptor that
    the ray meets first.

    The test cases are guaranteed so that the ray will meet a receptor
    eventually.
    '''
    # this confusing geometry pulled from discussion post by GSAN
    # https://leetcode.com/problems/mirror-reflection/discuss/938821/Python-pure-geometry-illustrated
    def mirrorReflection(self, p: int, q: int) -> int:
        k = 1
        while k * q % p:
            k += 1
        if k % 2 == 1 and (k * q // p) % 2 == 0:
            return 0
        if k % 2 == 1 and (k * q // p) % 2 == 1:
            return 1
        if k % 2 == 0 and (k * q // p) % 2 == 1:
            return 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 1
        o = 2
        self.assertEqual(s.mirrorReflection(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 1
        o = 1
        self.assertEqual(s.mirrorReflection(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)