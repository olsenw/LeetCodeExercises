# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A digit string is good if the digits (0-indexed) at even indices are even
    and the digits at odd indices are prime (2, 3, 5, or 7).

    Given an integer n, return the total number of good digit strings of length
    n. Since the answer may be large, return it modulo 10^9 + 7.

    A digit string is a string consisting of digits 0 through 9 that may contain
    leading zeros.
    '''
    # note the input range can be very large
    def countGoodNumbers_tle(self, n: int) -> int:
        m = 10**9 + 7
        answer = 1
        for i in range(n):
            pass
            # odd position
            if i % 2:
                answer = (answer * 4) % m
            # even position
            else:
                answer = (answer * 5) % m
        return answer

    # wrong - not multiplying each position correctly
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        odd, even = divmod(n, 2)
        even += odd
        odd = (odd * 4) % m
        even = (even * 5) % m
        return (odd * even) % m

    # important to use pow(base, exponent, mod) instead of (base ** exponent) % mod
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        odd, even = divmod(n, 2)
        even += odd
        return (pow(5, even, m) * pow(4, odd, m)) % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 5
        self.assertEqual(s.countGoodNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = 4
        o = 400
        self.assertEqual(s.countGoodNumbers(i), o)

    def test_three(self):
        s = Solution()
        i = 50
        o = 564908303
        self.assertEqual(s.countGoodNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)