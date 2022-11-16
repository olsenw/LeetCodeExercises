# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The Guessing game is played as follows:

    Player A picks a number between 1 and n. Player B guesses the number that
    Player A picked.

    Every time Player B guesses wrong Player A will tell them if their number is
    higher or lower than the guess.

    For this problem there is a predefined API which returns three possible
    results:
    * -1 if the guess is lower than the actual
    * 1 if the guess is greater than the actual
    * 0 if the guess is equal to the actual

    Acting as Player B, guess Player A's number using the API.
    '''
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        a = (high + low) // 2
        g = guess(a)
        while g != 0:
            if g > 0:
                low = a + 1
            else:
                high = a - 1
            a = (high + low) // 2
            g = guess(a)
        return a

class UnitTesting(unittest.TestCase):
    # tested in Leetcode
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)