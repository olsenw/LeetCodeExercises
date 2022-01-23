# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    An integer has sequential digits if and only if each digit in the
    number is one more than the previous digit.

    Return a sorted list of all the integers in the range [low,high]
    inclusive that have sequential digits.
    '''
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        import math
        s = []
        l = int(math.log10(low)) + 1
        h = int(math.log10(high)) + 1
        # how long sequential number should be
        for n in range(l, h+1):
            # starting digit
            for i in range(1,9):
                a = i
                for c in range(n-1):
                    i += 1
                    if i > 9:
                        break
                    a *= 10
                    a += i
                else:
                    if a > high:
                        return s
                    if a >= low:
                        s.append(a)
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 100
        h = 300
        o = [123,234]
        self.assertEqual(s.sequentialDigits(i,h), o)

    def test_two(self):
        s = Solution()
        i = 1000
        h = 13000
        o = [1234,2345,3456,4567,5678,6789,12345]
        self.assertEqual(s.sequentialDigits(i,h), o)

    def test_three(self):
        s = Solution()
        i = 10
        h = 99
        o = [12,23,34,45,56,67,78,89]
        self.assertEqual(s.sequentialDigits(i,h), o)

    def test_four(self):
        s = Solution()
        i = 58
        h = 156
        o = [67,78,89,123]
        self.assertEqual(s.sequentialDigits(i,h), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)