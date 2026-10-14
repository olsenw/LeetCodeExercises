# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers nums and sum.

    A positive integer n is good if it satisfies both of the following:
    * The number of digits in n is exactly num.
    * The sum of digits in n is exactly sum.

    The score of a good integer n is the sum of the squares of digits in n.

    Return a string denoting the good integer n that achieves the maximum score.
    If there are multiple possible integers, return the maximum one. If no such
    integer exists, return an empty string.
    '''
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""
        d,m = divmod(sum, 9)
        answer = "9" * d
        if m > 0:
            answer += str(m)
            d -= 1
        answer += "0" * (num - len(answer))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 3
        o = "30"
        self.assertEqual(s.maxSumOfSquares(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 17
        o = "98"
        self.assertEqual(s.maxSumOfSquares(i,j), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = 10
        o = ""
        self.assertEqual(s.maxSumOfSquares(i,j), o)

    def test_four(self):
        s = Solution()
        i = 1
        j = 9
        o = "9"
        self.assertEqual(s.maxSumOfSquares(i,j), o)

    def test_five(self):
        s = Solution()
        i = 2
        j = 18
        o = "99"
        self.assertEqual(s.maxSumOfSquares(i,j), o)

    def test_six(self):
        s = Solution()
        i = 2
        j = 9
        o = "90"
        self.assertEqual(s.maxSumOfSquares(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)