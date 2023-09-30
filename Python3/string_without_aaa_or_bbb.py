# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers a and b, return any string s such that:
    * s has length a + b and contains exactly a 'a' letters and exactly b 'b'
      letters,
    * The substring 'aaa' does not occur in s, and
    * The substring 'bbb' does not occur in s.
    '''
    def strWithout3a3b(self, a: int, b: int) -> str:
        answer = ""
        x, y = 'a', 'b'
        if b > a:
            a,b,x,y = b,a,y,x
        while a > 1:
            if a > b:
                answer += x + x
                a -= 2
            else:
                answer += x
                a -= 1
            if b:
                answer += y
                b -= 1
        if a:
            answer += x
        if b:
            answer += y
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1,2
        o = "bba"
        # o = "abb"
        self.assertEqual(s.strWithout3a3b(*i), o)

    def test_two(self):
        s = Solution()
        i = 4,1
        o = "aabaa"
        self.assertEqual(s.strWithout3a3b(*i), o)

    def test_three(self):
        s = Solution()
        i = 1,3
        o = "bbab"
        self.assertEqual(s.strWithout3a3b(*i), o)

    def test_four(self):
        s = Solution()
        i = 1,1
        o = "ab"
        self.assertEqual(s.strWithout3a3b(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)