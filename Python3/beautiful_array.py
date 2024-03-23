# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An array nums of length n is beautiful if:
    * nums is a permutation of the integers in the range [1, n].
    * For every 0 <= i < j < n, there is no index k with i < k < j where
      2 * nums[k] == nums[i] + nums[j].
    
    Given the integer n, return any beautiful array nums of length n. There will
    be at least one valid answer for the given n.
    '''
    # based on LeetCode solution
    # https://leetcode.com/problems/beautiful-array/editorial/
    # don't quite get why 
    def beautifulArray(self, n: int) -> List[int]:
        memo = {1: [1]}
        # divide and conquer
        def f(n):
            # don't need to do if answer already generated
            if n not in memo:
                # find permutation for smaller odd number range
                odds = f((n+1)//2)
                # find permutation for smaller even number range
                evens = f(n//2)
                # map sub ranges to new location
                memo[n] = [2 * i - 1 for i in odds] + [2 * i for i in evens]
            return memo[n]
        return f(n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = [2,1,4,3]
        self.assertEqual(s.beautifulArray(i), o)

    def test_two(self):
        s = Solution()
        i = 5
        o = [3,1,2,5,4]
        self.assertEqual(s.beautifulArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)