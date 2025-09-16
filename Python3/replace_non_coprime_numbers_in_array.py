# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums. Perform the following steps:
    1. Find any two adjacent numbers in nums that are non-coprime.
    2. If no such numbers are found, stop the process.
    3. Otherwise, delete the two numbers and replace them with their LCM (least
       common multiple).
    4) Repeat this process as long as there are at least two adjacent
       non-coprime numbers.
    
    Return the final modified array. If can be shown that replacing adjacent
    non-coprime numbers in any arbitrary order will lead to the same result.

    The test cases are generated such that the values in the final array are
    less than or equal to 10^9.

    Two values x and y are non-coprime if GCD(x,y) > 1 where GCD(x,y) is the
    greatest common divisor of x and y
    '''
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
        for n in nums:
            s.append(n)
            while len(s) > 1 and math.gcd(s[-2], s[-1]) > 1:
                # a = s.pop()
                # b = s.pop()
                # s.append(math.lcm(a,b))
                s.append(math.lcm(s.pop(), s.pop()))
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,4,3,2,7,6,2]
        o = [12,7,6]
        self.assertEqual(s.replaceNonCoprimes(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,1,1,3,3,3]
        o = [2,1,1,3]
        self.assertEqual(s.replaceNonCoprimes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)