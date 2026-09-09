# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    Return the total number of commas used when writing all integers from [1,n]
    (inclusive) in standard number formatting.

    In standard formatting:
    * A comma is inserted after every three digits from the right.
    * Numbers with fewer than 4 digits contain no commas.
    '''
    def countCommas_fails(self, n: int) -> int:
        segments = []
        t = n
        while t:
            t,r = divmod(t, 1000)
            segments.append(r)
        answer = 0
        commas = 1000
        for i in range(1,len(segments)):
            # answer += (segments[i] - 1) * commas * i + segments[0]
            # segments[0] += segments[i] * commas
            # commas *= 100
            answer += (segments[i] - 1) * commas
            answer += segments[0] * commas
            commas *= 100
            pass
        return answer

    # based on LeetCode editorial
    def countCommas(self, n: int) -> int:
        answer = 0
        comma = 1000
        # when commas being contributed are above number
        while comma <= n:
            # how many times this power of 10 contributed
            answer += n - comma + 1
            # increment the number of comma's contributed
            comma *= 1000
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1002
        o = 3
        self.assertEqual(s.countCommas(i), o)

    def test_two(self):
        s = Solution()
        i = 998
        o = 0
        self.assertEqual(s.countCommas(i), o)

    def test_three(self):
        s = Solution()
        i = 123456789
        o = 245912580
        self.assertEqual(s.countCommas(i), o)

    def test_four(self):
        s = Solution()
        i = 5378192
        o = 9755386
        self.assertEqual(s.countCommas(i), o)

    def test_five(self):
        s = Solution()
        i = 987654332221
        o = 2961961995666
        self.assertEqual(s.countCommas(i), o)

    def test_six(self):
        s = Solution()
        i = 456123
        o = 455124
        self.assertEqual(s.countCommas(i), o)

    def test_seven(self):
        s = Solution()
        i = 123000
        o = 122001
        self.assertEqual(s.countCommas(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)