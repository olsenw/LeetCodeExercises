# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n.

    Construct an array prefixGcd where for each index i:
    * Let mxi = max(nums[0], nums[1], ..., nums[i]).
    * prefixGcd[i] = gcd(nums[i], mxi)

    After constructing prefixGcd:
    * Sort prefixGcd in non-decreasing order.
    * Form pairs by taking the smallest unpaired element and the largest
      unpaired elements.
    * Repeat this process until no more pairs can be formed.
    * For each formed pair, compute the gcd of the two elements.
    * If n is odd, the middle element in the prefixGcd array remains unpaired
      and should be ignored.
    
    Return an integer denoting the sum of the GCD values of all formed pairs.

    The term gcd(a,b) denotes the greatest common divisor of a and b.
    '''
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0
        prefix = []
        for n in nums:
            mx = max(mx, n)
            prefix.append(math.gcd(n, mx))
        prefix.sort()
        i,j = 0, len(prefix) - 1
        answer = 0
        while i < j:
            answer += math.gcd(prefix[i], prefix[j])
            i += 1
            j -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,6,4]
        o = 2
        self.assertEqual(s.gcdSum(i), o)

    def test_two(self):
        s = Solution()
        i = [3,6,2,8]
        o = 5
        self.assertEqual(s.gcdSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)