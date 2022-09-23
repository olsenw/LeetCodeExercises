# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from math import log2

class Solution:
    '''
    Given an integer n, return the decimal value of the binary string formed by
    concatenating the binary representation of 1 to n in order, modulo 10^9 + 7.
    '''
    def concatenatedBinary_python_feature(self, n: int) -> int:
        return int("".join(bin(i)[2:] for i in range(n+1)),2) % (10**9 + 7)

    # based on discussion post by pankaj_777
    # https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/discuss/2612159/DAILY-LEETCODE-SOLUTION-oror-EASY-C%2B%2B-SOLUTION
    # this may be a better method to do this, by using integer that is twice as
    # large as two integers.
    # this allows two concatenated integers to fit in the variable.
    # doing a bit shift followed by an addition does the concatenation.
    # modulus follows the rules for modulus addition.
    def concatenatedBinary(self, n: int) -> int:
        m = 10**9 + 7
        a = 0
        for i in range(1, n+1):
            a = (a << (1 + int(log2(i)))) % m
            a = (a + i) % m
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.concatenatedBinary(i), o)

    def test_two(self):
        s = Solution()
        i = 3
        o = 27
        self.assertEqual(s.concatenatedBinary(i), o)

    def test_three(self):
        s = Solution()
        i = 12
        o = 505379714
        self.assertEqual(s.concatenatedBinary(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)