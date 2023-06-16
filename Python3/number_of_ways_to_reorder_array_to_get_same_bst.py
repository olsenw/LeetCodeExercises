# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import comb
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums that represents a permutation of integers from 1 to n.
    Construct a BST by inserting the the elements of nums in order into an
    initially empty BST. Find the number of different ways to reorder nums so
    that the constructed BST is identical to that formed from the original array
    nums.

    Return the number of ways to reorder nums such that the BST formed is
    identical to the original BST formed from nums.

    Since the answer may be very large, return it modulo 10^9+7.
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/editorial/
    # had the idea of the first node is always fixed and following nodes are
    # dependent. did not have the divide and conquer for rearranging values.
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9+7
        def dfs(nodes):
            m = len(nodes)
            if m < 3:
                return 1
            left = [i for i in nodes if i < nodes[0]]
            right = [i for i in nodes if i > nodes[0]]
            return dfs(left) * dfs(right) * comb(m - 1, len(left)) % mod
        return (dfs(nums) - 1) % mod

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3]
        o = 1
        self.assertEqual(s.numOfWays(i), o)

    def test_two(self):
        s = Solution()
        i = [3,4,5,1,2]
        o = 5
        self.assertEqual(s.numOfWays(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        o = 0
        self.assertEqual(s.numOfWays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)