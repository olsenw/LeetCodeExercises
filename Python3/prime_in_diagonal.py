# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed two-dimensional integer array nums.

    Return the largest prime number that lies on at least one of the diagonals
    of nums. In case, no prime is present on any of the diagonals, return 0.

    Note that:
    * An integer is prime if it is greater than 1 and has no positive integer
      divisors other than 1 and itself.
    * An integer val is on one of the diagonals of nums if there exists an
      integer i for which nums[i][i] = val or an i for which
      nums[i][nums.length - i - 1] = val.
    '''
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        # O(sqrt(n))
        def isPrime(num:int) -> bool:
            if num <= 2:
                return num == 2
            for i in range(2, math.ceil(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        answer = 0
        n = len(nums)
        for i in range(n):
            if isPrime(nums[i][i]):
                answer = max(answer, nums[i][i])
            if isPrime(nums[i][n-i-1]):
                answer = max(answer, nums[i][n-i-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[5,6,7],[9,10,11]]
        o = 11
        self.assertEqual(s.diagonalPrime(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[5,17,7],[9,11,10]]
        o = 17
        self.assertEqual(s.diagonalPrime(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)