# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    A path in a binary tree is a sequence of nodes where each pair of adjacent
    nodes in the sequence has an edge connecting them. A node can only appear in
    the sequence at most once. Note that the path does not need to pass through
    the root.
    
    The path sum of a path is the sum of the node's values in the path.
    
    Given the root of a binary tree, return the maximum path sum of any
    non-empty path.
    '''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -1000
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best
            best = max(best, node.val)
            if not node.left and not node.right:
                return node.val
            l = dfs(node.left) if node.left else 0
            best = max(best, node.val + l)
            r = dfs(node.right) if node.right else 0
            best = max(best, node.val + r)
            best = max(best, node.val + l + r)
            return node.val + max(l, r, 0)
        return max(dfs(root), best)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        o = 6
        self.assertEqual(s.maxPathSum(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        o = 42
        self.assertEqual(s.maxPathSum(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(-2, TreeNode(1))
        o = 1
        self.assertEqual(s.maxPathSum(i), o)

    def test_four(self):
        s = Solution()
        i = TreeNode(9, TreeNode(6), TreeNode(-3, TreeNode(-6), TreeNode(2, TreeNode(2, TreeNode(-6, TreeNode(-6)), TreeNode(-6)))))
        o = 16
        self.assertEqual(s.maxPathSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)