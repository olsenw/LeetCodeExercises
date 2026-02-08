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
    A binary tree is uni-valued if every node in the tree has the same value.

    Given the root of a binary tree, return true if the tree is uni-valued or
    false otherwise.
    '''
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode], value:int) -> bool:
            if node is None:
                return True
            return node.val == value and dfs(node.left, value) and dfs(node.right, value)
        return dfs(root.left, root.val) and dfs(root.right, root.val)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
        o = True
        self.assertEqual(s.isUnivalTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(2, TreeNode(2, TreeNode(5), TreeNode(2)), TreeNode(2))
        o = False
        self.assertEqual(s.isUnivalTree(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = True
        self.assertEqual(s.isUnivalTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)