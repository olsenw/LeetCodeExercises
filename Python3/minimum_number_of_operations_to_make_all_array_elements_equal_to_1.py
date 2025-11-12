# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums consisting of positive integers. The following
    operation can be preformed on the array any number of times:
    * Select an index i such that 0 <= i <= n - 1 and replace either of nums[i]
      or nums[i+1] with their gcd value.
    
    Return the minimum number of operations to make all elements of nums equal
    to 1. If it is impossible, return -1.

    The gcd of two integers is the greatest common divisor of the two integers.
    '''
    def minOperations_thinking(self, nums: List[int]) -> int:
        def isPrime(num: int) -> bool:
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        n = len(nums)
        s = set()
        for i in range(n-1):
            gcd = math.gcd(nums[i], nums[i+1])
            s.add(gcd)
            # if gcd == 1 or isPrime(gcd):
                # s.add(gcd)
        return

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        # test if possible
        if math.gcd(*nums) > 1:
            return -1
        def bestArray():
            for w in range(2, n+1):
                for i in range(n - w + 1):
                    if math.gcd(*nums[i:i+w]) == 1:
                        return i,w
        index, width = bestArray()
        answer = 2 * (width - 1)
        return n - width + answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,6,3,4]
        o = 4
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [2,10,6,14]
        o = -1
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [30,60,90]
        o = -1
        self.assertEqual(s.minOperations(i), o)

    def test_four(self):
        s = Solution()
        i = [15,30,60]
        o = -1
        self.assertEqual(s.minOperations(i), o)

    def test_five(self):
        s = Solution()
        i = [2,14,28,7]
        o = 6
        self.assertEqual(s.minOperations(i), o)

    def test_six(self):
        s = Solution()
        i = [1,1]
        o = 0
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)