# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    The score of n is defined as the sum of d * freq(d) over all distinct digits
    d, where freq(d) denotes the number of times the digit d appears in n.

    Return an integer denoting the score of n.
    '''
    def digitFrequencyScore(self, n: int) -> int:
        c = Counter(str(n))
        return sum(int(i) * c[i] for i in c)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 122
        o = 5
        self.assertEqual(s.digitFrequencyScore(i), o)

    def test_two(self):
        s = Solution()
        i = 101
        o = 2
        self.assertEqual(s.digitFrequencyScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)