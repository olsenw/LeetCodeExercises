# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers left and right, find the two integers num1 and
    num2 such that:
    * left <= num1 < num2 <= right
    * Both num1 and num2 are prime numbers
    * num2 - num1 is the minimum amongst all other pairs satisfying the above
      conditions.
    
    Return the positive integer array ans = [num1, num2]. If there are multiple
    pairs satisfying these conditions, return the one with the smallest num1
    value. If no such numbers exist, return [-1, -1].
    '''
    # based on hints
    # brute force search primes in range
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        def eratosthenes(n:int)->List[int]:
            a = [True] * (n+1)
            a[0] = False
            a[1] = False
            for i in range(2, math.isqrt(n)+1):
                if a[i]:
                    for j in range(i*i,n+1,i):
                        a[j] = False
            return [i for i in range(2, n+1) if a[i]]
        primes = eratosthenes(right)
        m = right + 1
        answer = [-1,-1]
        for i in range(len(primes)-2,-1,-1):
            if primes[i] < left:
                break
            if m >= primes[i+1] - primes[i]:
                m = primes[i+1] - primes[i]
                answer = [primes[i], primes[i+1]]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        j = 19
        o = [11, 13]
        self.assertEqual(s.closestPrimes(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = 6
        o = [-1, -1]
        self.assertEqual(s.closestPrimes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)