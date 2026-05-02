# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An integer x is good if after rotating each digit individually by 180
    degrees, it becomes a valid number different from x. Each digit must be
    rotated, it cannot be left alone.

    A number is valid if each digit remains a digit after rotation. For example:
    * 0, 1, and 8 rotate to themselves.
    * 2 and 5 rotate to each other (in this case they are rotated in a different
      direction, in other words, 2 or 5 gets mirrored).
    * 6 and 9 rotate to each other, and
    * the rest of the numbers do not rotate to any other number and become
      invalid.

    Given an integer n, return the number of good integers in the range [1, n].
    '''
    @cache
    def rotatedDigits(self, n: int) -> int:
        if n == 1:
            return 0
        rotate = {
            '0':'0',
            '1':'1',
            '8':'8',
            '2':'5',
            '5':'2',
            '6':'9',
            '9':'6'
        }
        answer = ""
        for c in str(n):
            if c in rotate:
                answer += rotate[c]
            else:
                answer += 'n'
                break
        if answer[-1] == 'n':
            answer = 0
        else:
            answer = int(str(answer)) != n
        return answer + self.rotatedDigits(n-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        o = 4
        self.assertEqual(s.rotatedDigits(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 0
        self.assertEqual(s.rotatedDigits(i), o)

    def test_three(self):
        s = Solution()
        i = 2
        o = 1
        self.assertEqual(s.rotatedDigits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)