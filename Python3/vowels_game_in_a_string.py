# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob are playing a game on a string.

    Given a sting s, Alice and Bob will take turn playing the following game
    where Alice starts first:
    * On Alice's turn, she has to remove any non-empty substring from s that
      contains an odd number of vowels.
    * On Bob's turn, he has to remove any non-empty substring from s that
      contains an even number of vowels.

    The first player who cannot make a move on their turn loses the game. We
    assume that both Alice and Bob play optimally.

    Return true if Alice wins the game, and false otherwise.

    The English vowels are: a, e, i, o, and u.
    '''
    def doesAliceWin(self, s: str) -> bool:
        # only way alice can lose is if there are no vowels to take
        return sum(c in "aeiou" for c in s) != 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leetcoder"
        o = True
        self.assertEqual(s.doesAliceWin(i), o)

    def test_two(self):
        s = Solution()
        i = "bbcd"
        o = False
        self.assertEqual(s.doesAliceWin(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)