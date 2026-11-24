# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums.

    An array arr is called product equivalent if prod(arr) = lcm(arr) * gcd(arr)
    where:
    * prod(arr) is the products of all elements of arr.
    * gcd(arr) is the GCD of all elements of arr.
    * lcm(arr) is the LCM of all elements of arr.

    Return the length of the longest product equivalent subarray of nums.
    '''
    # brute force
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            p = 1
            l = nums[i]
            for j in range(i,n):
                p *= nums[j]
                g = math.gcd(*nums[i:j+1])
                # l = math.lcm(*nums[i:j+1])
                l = math.lcm(l, nums[j])
                if p == g * l:
                    answer = max(answer, j-i+1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1,2,1,1,1]
        o = 5
        self.assertEqual(s.maxLength(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4,5,6]
        o = 3
        self.assertEqual(s.maxLength(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,1,4,5,1]
        o = 5
        self.assertEqual(s.maxLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)