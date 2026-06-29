# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    Let r be the integer formed by reversing the digits of n.

    Return the sum of all prime numbers between min(n,r) and max(n,r),
    inclusive.
    '''
    def sumOfPrimesInRange(self, n: int) -> int:
        def isPrime(n:int) -> bool:
            if n == 1:
                return False
            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    return False
            return True
        r = int(str(n)[::-1])
        answer = 0
        for i in range(min(n,r),max(n,r)+1):
            if isPrime(i):
                answer += i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 13
        o = 132
        self.assertEqual(s.sumOfPrimesInRange(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 17
        self.assertEqual(s.sumOfPrimesInRange(i), o)

    def test_three(self):
        s = Solution()
        i = 8
        o = 0
        self.assertEqual(s.sumOfPrimesInRange(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)