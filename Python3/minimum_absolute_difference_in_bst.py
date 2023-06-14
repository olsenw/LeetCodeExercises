# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
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
    Given the root of a Binary Search Tree (BST), return the minimum absolute
    difference between the values of any two different nodes in the tree.
    '''
    # same answer as #783 minimum distance between bst nodes
    def getMinimumDifference_783(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return min(values[i] - values[i-1] for i in range(1, len(values)))

    # based on Editorial (does away with the list)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.m = 10**9 + 1
        self.prev = None
        def dfs(node:Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            if self.prev is not None:
                self.m = min(self.m, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)
            return
        dfs(root)
        return self.m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        o = 1
        self.assertEqual(s.getMinimumDifference(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
        o = 1
        self.assertEqual(s.getMinimumDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)