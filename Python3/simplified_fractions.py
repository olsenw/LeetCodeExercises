# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

class Solution:
    '''
    Given an integer n, return a list of all simplified fractions between 0 and
    1 (exclusive) such that the denominator is less than or equal to n. The
    answer may be returned in any order.
    '''
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = set()
        for i in range(2,n+1):
            for j in range(1,i):
                g = math.gcd(j,i)
                fractions.add((j // g, i // g))
        return [f'{i}/{j}' for i,j in fractions]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = ["1/2"]
        self.assertEqual(sorted(s.simplifiedFractions(i)), o)

    def test_two(self):
        s = Solution()
        i = 3
        o = ["1/2","1/3","2/3"]
        self.assertEqual(sorted(s.simplifiedFractions(i)), o)

    def test_three(self):
        s = Solution()
        i = 4
        o = ["1/2","1/3","1/4","2/3","3/4"]
        self.assertEqual(sorted(s.simplifiedFractions(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)