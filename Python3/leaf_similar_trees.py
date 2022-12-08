# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
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
    Consider all the leaves of a binary tree, from left to right order, the 
    values of those leaves form a leaf value sequence.
    
    Two binary trees are considered leaf-similar if their leaf value sequence is
    the same.

    Return True if and only if the two given trees with head nodes root1 and
    root2 are leaf-similar.
    '''
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def r(node:TreeNode):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from r(node.left)
            if node.right:
                yield from r(node.right)
        return all(i == j for i,j in zip_longest(r(root1), r(root2)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        j = TreeNode(1, TreeNode(2), TreeNode(3))
        o = True
        self.assertEqual(s.leafSimilar(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        j = TreeNode(1, TreeNode(3), TreeNode(2))
        o = False
        self.assertEqual(s.leafSimilar(i,j), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        j = TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3), TreeNode(1)))
        o = False
        self.assertEqual(s.leafSimilar(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)