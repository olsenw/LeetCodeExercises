# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import isqrt, sqrt
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the sum of divisors of the integers in
    that array that have exactly four divisors. If there is no such integer in
    the array, return 0.
    '''
    def sumFourDivisors_fails(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            a = 0
            s = 0
            for i in range(1, isqrt(n)):
                if n % i == 0:
                    a += 2
                    s += i
                    s += n // i
                if a > 4:
                    break
            if a == 4:
                answer += s
        return answer

    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            s = set()
            for i in range(1, isqrt(n)+1):
                if n % i == 0:
                    s.add(i)
                    s.add(n // i)
                if len(s) > 4:
                    break
            if len(s) == 4:
                answer += sum(s)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [21,4,7]
        o = 32
        self.assertEqual(s.sumFourDivisors(i), o)

    def test_two(self):
        s = Solution()
        i = [21,21]
        o = 64
        self.assertEqual(s.sumFourDivisors(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 0
        self.assertEqual(s.sumFourDivisors(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,10]
        o = 45
        self.assertEqual(s.sumFourDivisors(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)