# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers left and right, return the count of numbers in the
    inclusive range [left, right] having a prime number of set bits in their
    binary representation.

    Recall that the number of set bits an integer has is the number of 1's
    present when written in binary.
    '''
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n:int) -> bool:
            if n <= 1:
                return False
            answer = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    answer = False
                    break
            return answer
        answer = 0
        for i in range(left, right+1):
            answer += isPrime(bin(i).count("1"))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = 10
        o = 4
        self.assertEqual(s.countPrimeSetBits(i,j), o)

    def test_two(self):
        s = Solution()
        i = 10
        j = 15
        o = 5
        self.assertEqual(s.countPrimeSetBits(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)