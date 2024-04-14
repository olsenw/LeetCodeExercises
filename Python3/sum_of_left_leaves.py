# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree, return the sum of all left leaves.

    A leaf is a node with no children. A left leaf is a leaf that is the left
    child of another node.
    '''
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], left: bool):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val if left else 0
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        o = 24
        self.assertEqual(s.sumOfLeftLeaves(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        o = 0
        self.assertEqual(s.sumOfLeftLeaves(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)