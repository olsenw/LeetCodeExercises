# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer num, return a string of its base 7 representation
    '''
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg = num < 0
        if neg:
            num = -num
        answer = []
        while num != 0:
            answer.append(str(num % 7))
            num //= 7
        return f'{"-" if neg else ""}{"".join(answer[::-1])}'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 100
        o = "202"
        self.assertEqual(s.convertToBase7(i), o)

    def test_two(self):
        s = Solution()
        i = -7
        o = "-10"
        self.assertEqual(s.convertToBase7(i), o)

    def test_three(self):
        s = Solution()
        i = -7
        o = "-10"
        self.assertEqual(s.convertToBase7(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)