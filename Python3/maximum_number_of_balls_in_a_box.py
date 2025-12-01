# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    There are n balls numbered from lowLimit up to highLimit inclusive
    (n == highLimit - lowLimit + 1), and an infinite number of boxes numbered 1
    to infinity.

    Put each ball in the box with a number equal to the sum of digits of the
    ball's number. (ball 321 -> 3 + 2 + 1 = 6 -> box 6)

    Given two integers lowLimit and highLimit, return the number of balls in the
    box with the most balls.
    '''
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = Counter()
        for ball in range(lowLimit, highLimit + 1):
            box = 0
            while ball:
                d,m = divmod(ball, 10)
                box += m
                ball = d
            c[box] += 1
        return c.most_common(1)[0][1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 10
        o = 2
        self.assertEqual(s.countBalls(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 15
        o = 2
        self.assertEqual(s.countBalls(i,j), o)

    def test_one(self):
        s = Solution()
        i = 19
        j = 28
        o = 2
        self.assertEqual(s.countBalls(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)