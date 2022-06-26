# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are several cards arranged in a row, and each card has an
    associated number of points. The points are given in the integer
    array cardPoints.

    In one step, a card may be taken from the beginning or end of the
    row. It is required to take k cards.

    The score is the sum of the points of the taken cards.

    Given the integer array cardPoints and the integer k, return the
    maximum score that can be obtained.
    '''
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        c = b = sum(cardPoints[:k])
        i = len(cardPoints) - 1
        j = k - 1
        while j >= 0:
            c += cardPoints[i] - cardPoints[j]
            b = max(b, c)
            i -= 1
            j -= 1
        return b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5,6,1]
        j = 3
        o = 12
        self.assertEqual(s.maxScore(i, j), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2]
        j = 2
        o = 4
        self.assertEqual(s.maxScore(i, j), o)

    def test_three(self):
        s = Solution()
        i = [9,7,7,9,7,7,9]
        j = 7
        o = 55
        self.assertEqual(s.maxScore(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)