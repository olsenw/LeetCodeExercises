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
    Given an integer n, return all the structurally unique BST's (binary search
    trees), which has exactly n nodes of unique values from 1 to n. Return the
    answer in any order.
    '''
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def clone(root):
            if root == None:
                return None
            return TreeNode(root.val, clone(root.left), clone(root.right))
        @cache
        def dp(low, high):
            if high < low:
                return [None]
            if low == high:
                return [TreeNode(low)]
            answer = []
            for i in range(low, high + 1):
                left = dp(low, i - 1)
                right = dp(i + 1, high)
                for j in left:
                    for k in right:
                        answer.append(TreeNode(i, clone(j), clone(k)))
            return answer
        answer = dp(1,n)
        return answer

class UnitTesting(unittest.TestCase):
    '''
    Tested online
    '''
    def test_one(self):
        s = Solution()
        s.generateTrees(3)
        # self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)