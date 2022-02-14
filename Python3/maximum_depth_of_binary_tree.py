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
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the
    longest path from the root node down to the farthest leaf node.
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l,r)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        o = 3
        self.assertEqual(s.maxDepth(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(2))
        o = 2
        self.assertEqual(s.maxDepth(i), o)

    def test_three(self):
        s = Solution()
        i = None
        o = 0
        self.assertEqual(s.maxDepth(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)