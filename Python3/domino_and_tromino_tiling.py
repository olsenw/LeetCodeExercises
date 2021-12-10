# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer n return the number of ways to tile a 2 x n board.

    Given two types of tiles a 2 x 1 and a tromino shape which may be
    rotated.

    0   00  00  00   0  0
    0       0    0  00  00
    a   b   c   d   e   f

    In tiling every square must be covered by a tile. Two tilings are
    different if and only if there are two 4-directionally adjacent
    cells on the board such that exactly one of the tilings has both
    squares occupied by a tile.

    Return the answer modulo (10**9 + 7).
    '''
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        modulo = 10**9 + 7

        dN = 0
        dN1 = 5
        dN2 = 2
        dN3 = 1

        print(n)
        for i in range(4, n+1):
            dN = ((2 * dN1) + (dN3))
            print(i, dN, dN1, dN2, dN3)
            dN3 = dN2
            dN2 = dN1
            dN1 = dN

        return dN % modulo

'''
This works due how tiles can be interatvely added at end.

There are four patterns that can be added to the end of the board.

a which is added to the end
    *****|0
    *****|0
b which is added to the last two
    ****|00
    ****|00
c which is added as a pattern of various length (note it can be flipped
  upsidedown)
    ***|00 0    ***|00 00 0     ***|00 00 00 00 0
    ***|0 00    ***|0 00 00     ***|0 00 00 00 00
d which is also added as pattern (note also can be flipped upsidedown)
    ***|00  00  ***|00 00  00   ***|00 00 00  00
    ***|0 00 0  ***|0 00 00 0   ***|0 00 00 00 0

These are as added up as a series
a) Tn = Tn-1
b) Tn = Tn-2
c) Tn = Tn-3 + Tn-5 + Tn-7 + ... T1 or T0   (will double because flip)
d) Tn = Tn-4 + Tn-6 + Tn-8 + ... T1 or T0   (will double because flip)

So in total
Tn = 2 summation(Ti, 0, N-1) + Tn-2 + Tn-1
Tn = 2 Tn-1 + Tn-3
'''

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.numTilings(3), 5)

    def test_two(self):
        s = Solution()
        self.assertEqual(s.numTilings(1), 1)

    def test_three(self):
        s = Solution()
        self.assertEqual(s.numTilings(4), 11)

    def test_four(self):
        s = Solution()
        self.assertEqual(s.numTilings(5), 24)

if __name__ == '__main__':
    unittest.main(verbosity=2)