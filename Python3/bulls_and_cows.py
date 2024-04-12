# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Play a game called Bulls and Cows.

    Write down a secret number and ask the opponent to guess what the number is.
    When the opponent makes a guess, provide a hint with the following info.
    * The number of "bulls", which are digits in the guess that are in the
      correct position.
    * The number of "cows", which are digits in the guess that are in the secret
      number but are located in the wrong position. Specifically, the non-bull
      digits in the guess that could be rearranged such that they become bulls.
    
    Given the secret number secret and the opponent's guess guess, return the
    hint for the opponents guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y
    is the number of cows. Note that both secret and guess may contain duplicate
    digits. 
    '''
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        c = Counter(secret)
        cows = Counter()
        for i,j in zip(guess[::-1],secret[::-1]):
            if i == j:
                bulls += 1
                c[i] -= 1
            else:
                cows[i] += 1
        cows = sum(min(c[i], cows[i]) for i in c)
        return f'{bulls}A{cows}B'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1807"
        j = "7810"
        o = "1A3B"
        self.assertEqual(s.getHint(i,j), o)

    def test_two(self):
        s = Solution()
        i = "1123"
        j = "0111"
        o = "1A1B"
        self.assertEqual(s.getHint(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)