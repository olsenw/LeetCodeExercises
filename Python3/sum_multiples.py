# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, return the sum of all integers in the range
    [1, n] inclusive that are divisible by 3,5, or 7.

    Return an integer denoting the sum of all numbers in the given range
    satisfying the constraint.
    '''
    def sumOfMultiples(self, n: int) -> int:
        answer = 0
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                answer += i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 7
        o = 21
        self.assertEqual(s.sumOfMultiples(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 40
        self.assertEqual(s.sumOfMultiples(i), o)

    def test_three(self):
        s = Solution()
        i = 9
        o = 30
        self.assertEqual(s.sumOfMultiples(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)