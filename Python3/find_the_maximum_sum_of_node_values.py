# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There exists an undirected tree with n nodes numbered 0 to n - 1. Given a
    0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi]
    indicates that there is an edge between nodes ui and vi in the tree. Also
    given a positive integer k, and a 0-indexed array of non-negative integers
    nums of length n, where nums[i] represents the value of the node numbered i.

    Alice wants the sum of values of tree nodes to be maximum, for which Alice
    can perform the following operation any number of times (including zero) on
    the tree:
    * Choose any edge [u, v] connecting the nodes u and v and update the value
      as follows
      * nums[u] = nums[u] XOR k
      * nums[v] = nums[v] XOR k
    
    Return the maximum possible sum of the values Alice can achieve by
    performing the operation any number of times.
    '''
    # based on leetcode editorial greedy solution
    # https://leetcode.com/problems/find-the-maximum-sum-of-node-values/editorial/?envType=daily-question&envId=2024-05-19
    # important note is that any two nodes can be xor with k by chaining xor
    # along path from first to second node
    # sort the change in value each node can have if xor is applied
    # add the change by pairing up the most valuable nodes
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        changes = sorted([(n ^ k) - n for n in nums],reverse=True)
        answer = sum(nums)
        for i in range(0, len(nums)-1, 2):
            t = changes[i] + changes[i+1]
            if t >= 0:
                answer += t
            else:
                break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1]
        j = 3
        k = [[0,1],[0,2]]
        o = 6
        self.assertEqual(s.maximumValueSum(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [2,3]
        j = 7
        k = [[0,1]]
        o = 9
        self.assertEqual(s.maximumValueSum(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [7,7,7,7,7,7]
        j = 3
        k = [[0,1],[0,2],[0,3],[0,4],[0,5]]
        o = 42
        self.assertEqual(s.maximumValueSum(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)