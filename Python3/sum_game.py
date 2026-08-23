# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob take turns playing a game, with Alice starting first.

    Given a string num of even length consisting of digits and '?' characters.
    On each turn, a player will do the following if there is still at least one
    '?' in num:
    1) Choose an index i where num[i] == '?'.
    2) Replace num[i] with any digit between '0' and '9'.

    The game ends when there are no more '?' character in num.

    For Bob to win, the sum of the digits in the first half of num must be equal
    to the sum of the digits in the second half. For Alice to win, the sums must
    not be equal.

    Assuming Alice and Bob play optimally, return true if Alice will win and
    false if Bob will win.
    '''
    def sumGame_incomplete(self, num: str) -> bool:
        left,right = 0,0
        leftQuestion, rightQuestion = 0,0
        for n in num[:len(num)//2]:
            if n == '?':
                leftQuestion += 1
            else:
                left += int(n)
        for n in num[len(num)//2:]:
            if n == '?':
                rightQuestion += 1
            else:
                right += int(n)
        alice = True
        while leftQuestion or rightQuestion:
            if alice:
                pass
            else:
                pass
            alice = not alice
        return left != right

    # Based on Leetcode editorial
    # https://leetcode.com/problems/sum-game/editorial/?envType=daily-question&envId=2026-08-23
    def sumGame(self, num: str) -> bool:
        left,right = 0,0
        leftQuestion, rightQuestion = 0,0
        for n in num[:len(num)//2]:
            if n == '?':
                leftQuestion += 1
            else:
                left += int(n)
        for n in num[len(num)//2:]:
            if n == '?':
                rightQuestion += 1
            else:
                right += int(n)
        # Alice will always win if there are a odd number of questions
        if (leftQuestion + rightQuestion) % 2 == 1:
            return True
        # difference of current value cannot be matched with questions
        # note left right and question left right are crossed
        if left - right != (rightQuestion - leftQuestion) * 9 // 2:
            return True
        # Bob wins
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "5023"
        o = False
        self.assertEqual(s.sumGame(i), o)

    def test_two(self):
        s = Solution()
        i = "25??"
        o = True
        self.assertEqual(s.sumGame(i), o)

    def test_two(self):
        s = Solution()
        i = "?3295???"
        o = False
        self.assertEqual(s.sumGame(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)