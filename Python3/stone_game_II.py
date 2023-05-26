# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob continue their games with piles of stones. There are a number
    of piles arranged in a row, and each pile has a positive integer number of
    stones piles[i]. The objective of the game is to end with the most stones.

    Alice and Bob take turns, with Alice starting first. Initially M = 1.

    On each players turn, that player can take all the stones in the first X
    remaining piles, where 1 <= X <= 2M. Then M is set to max(M, X).

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones
    Alice can get.
    '''
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def dp(a, i, m):
            if i == n:
                return 0
            # if bob turn want to minimize if alice turn maximize
            answer = 1000000 if a == 1 else 0
            # running sum of the piles being considered
            s = 0
            for j in range(1, min(2 * m, n - i) + 1):
                s += piles[i + j - 1]
                if a == 0:
                    answer = max(
                        answer,
                        s + dp(1, i + j, max(m, j))
                    )
                else:
                    answer = min(
                        answer,
                        dp(0, i + j, max(m,j))
                    )
            return answer
        return dp(0,0,1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,7,9,4,4]
        o = 10
        self.assertEqual(s.stoneGameII(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5,100]
        o = 104
        self.assertEqual(s.stoneGameII(i), o)

    def test_three(self):
        s = Solution()
        i = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063,8023,7729,7084,8407]
        o = 98008
        self.assertEqual(s.stoneGameII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)