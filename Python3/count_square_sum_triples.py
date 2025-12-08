# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A square triple (a,b,c) is a triples where a, b, and c are integers and
    a^2 + b^2 = c^2.

    Given an integer n, return the number of square triples such that
    1 <= b, b, c <= n.
    '''
    def countTriples_tle(self, n: int) -> int:
        answer = 0
        for i in range(1, n+1):
            a = i * i
            for j in range(1, n+1):
                b = j * j
                for k in range(1, n+1):
                    c = k * k
                    if a + b == c:
                        answer += 1
                    if a + b <= c:
                        break
        return answer

    def countTriples(self, n: int) -> int:
        answer = 0
        for i in range(1, n+1):
            a = i * i
            for j in range(i, n+1):
                b = j * j
                c = math.isqrt(a + b)
                if c <= n and a + b == c * c:
                    answer += 2
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = 2
        self.assertEqual(s.countTriples(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 4
        self.assertEqual(s.countTriples(i), o)

    def test_three(self):
        s = Solution()
        i = 234
        o = 308
        self.assertEqual(s.countTriples(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)