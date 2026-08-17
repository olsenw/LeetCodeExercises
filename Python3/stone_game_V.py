# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are several stones arranged in a row, and each stone has an associated
    value which is an integer given in the array stoneValue.

    In each round of the game, Alice divides the row into two non-empty rows (ie
    left row and right row), then Bob calculates the value of each row which is
    the sum of the values of all the stones in this row. Bob throws away the row
    which has the maximum value, and Alice's score increases by the value of the
    remaining row. If the value of the two rows are equal, Bob lets Alice decide
    which row will be thrown away. The next round starts with the remaining row.

    The game ends when there is only one stone remaining. Alice's score is
    initially zero.

    Return the maximum score that Alice can obtain.
    '''
    def stoneGameV_incomplete(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue))
        @cache
        def dp(left:int, right:int):
            if left == right:
                return 0
            for i in range(left,right + 1):
                a = prefix[i] if left == 0 else prefix[i] - prefix[left - 1]
                b = prefix[right] if right - 1 else prefix[right] - prefix[i + 1]
            return
        return dp(0,len(stoneValue) - 1)

    def stoneGameV(self, stoneValue: List[int]) -> int:
        @cache
        def dp(i:int, j:int) -> int:
            if i == j:
                return 0
            s = sum(stoneValue[i:j+1])
            score = 0
            left = 0
            for k in range(i,j):
                left += stoneValue[k]
                right = s - left
                if left < right:
                    score = max(score, left + dp(i,k))
                elif left > right:
                    score = max(score, right + dp(k+1,j))
                else:
                    score = max(score, left + dp(i,k), right + dp(k+1,j))
            return score
        return dp(0, len(stoneValue) - 1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,2,3,4,5,5]
        o = 18
        self.assertEqual(s.stoneGameV(i), o)

    def test_two(self):
        s = Solution()
        i = [7,7,7,7,7,7,7]
        o = 28
        self.assertEqual(s.stoneGameV(i), o)

    def test_two(self):
        s = Solution()
        i = [4]
        o = 0
        self.assertEqual(s.stoneGameV(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)