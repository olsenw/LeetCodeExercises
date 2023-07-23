# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given an integer n, return a list of all possible full binary trees with n
    nodes. Each node of each tree in the answer must have node.val == 0.

    Each element of the is the root node of one possible tree. The final list
    may be returned in any order.

    A full binary tree is a binary tree where each node has exactly 0 or 2
    children.
    '''
    # this errors due to creating cycles...
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # should bail on odd cases
        if n == 1:
            return [TreeNode(0)]
        answer = []
        n -= 1
        for i in range(1, n, 2):
            a = self.allPossibleFBT(i)
            b = self.allPossibleFBT(n-i)
            if a and b:
                # iteration wrong here... need to iterate all options in a and b
                answer.append(TreeNode(0, a, b))
        return answer

    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # only works for an odd number of nodes
        if n % 2 == 0:
            return []
        # base case
        if n == 1:
            return [TreeNode(0)]
        answer = []
        # iterate odd numbers to each side
        for i in range(1, n, 2):
            a = self.allPossibleFBT(i)
            b = self.allPossibleFBT(n - i - 1)
            for j in a:
                for k in b:
                    answer.append(TreeNode(0, j, k))
        return answer
        

class UnitTesting(unittest.TestCase):
    '''
    Tested using the LeetCode
    '''
    # def test_one(self):
    #     s = Solution()
    #     i = [1,2,3,4,5]
    #     o = 5
    #     self.assertEqual(s.problem_name(i), o)

    # def test_two(self):
    #     s = Solution()
    #     i = [1,2,3,4,5]
    #     o = 5
    #     self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)