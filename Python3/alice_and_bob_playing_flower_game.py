# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob are playing a turn-based game on a field with two lanes of
    flowers between them. There are x flowers in the first land between Alice
    and Bob, and y flowers in the second lane between them.

    The game proceeds as follows:
    1) Alice takes the first turn.
    2) In each turn, a player must choose either one of the lanes and pick one
       flower from that lane.
    3) At the end of the turn, if there aer no flowers left at all, the current
       player captures their opponent and wins the game.

    Given two integers, n and m, the task is to computer the number of possible
    pairs (x, y) that satisfy the conditions:
    * Alice must win the game according to the described rules.
    * The number of flowers x in the first lane must be in the range [1,n].
    * The number of flowers y in the second lane must be in the range [1,m].

    Return the number of possible pairs (x,y) that satisfy the conditions
    mentioned in the statement.
    '''
    # O(n * m)
    def flowerGame_brute(self, n: int, m: int) -> int:
        answer = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                answer += (i + j) % 2
        return answer

    def flowerGame(self, n: int, m: int) -> int:
        nEven = n // 2
        nOdd  = (n // 2) + (n % 2)
        mEven = m // 2
        mOdd  = (m // 2) + (m % 2)
        return (nOdd * mEven) + (nEven * mOdd)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 2
        o = 3
        self.assertEqual(s.flowerGame(i,j), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = 1
        o = 0
        self.assertEqual(s.flowerGame(i,j), o)

    def test_three(self):
        s = Solution()
        i = 10012
        j = 22114
        o = 110702684
        self.assertEqual(s.flowerGame(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)