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
    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right

class Solution:
    '''
    Given the root of a binary tree, return the same tree where every
    subtree (of the given tree) not containing a 1 has been removed.

    A subtree of a node node is node plus every node that is a
    descendant of node.
    '''
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return False
            if not dfs(node.left):
                node.left = None
            if not dfs(node.right):
                node.right = None
            return node.val == 1 or node.left or node.right
        return root if dfs(root) else None

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
        o = TreeNode(1, None, TreeNode(0, None, TreeNode(1)))
        self.assertEqual(s.pruneTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
        o = TreeNode(1, None, TreeNode(1, None, TreeNode(1)))
        self.assertEqual(s.pruneTree(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1,TreeNode(1,TreeNode(1,TreeNode(0)),TreeNode(1)),TreeNode(0, TreeNode(0), TreeNode(1)))
        o = TreeNode(1,TreeNode(1,TreeNode(1),TreeNode(1)),TreeNode(0, None, TreeNode(1)))
        self.assertEqual(s.pruneTree(i), o)

    def test_four(self):
        s = Solution()
        i = TreeNode(0,None,TreeNode(0,TreeNode(0),TreeNode(0)))
        o = None
        self.assertEqual(s.pruneTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)