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
    For a binary tree T, the flip operation can be defined as follows: choose
    any node, and swap the left and right child subtrees.

    A binary tree X is flip equivalent to a binary tree Y if and only if X is
    equal to Y after some number of flip operations.

    Given the roots of two binary tree root1 and root2, return true if the two
    trees are flip equivalent or false otherwise.
    '''
    # believe that this passes... but getting an incorrect time on LeetCode
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None or root2 is None:
            return root1 is None and root2 is None
        if root1.val == root2.val:
            return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
        j = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7))))
        o = True
        self.assertEqual(s.flipEquiv(i,j), o)

    def test_two(self):
        s = Solution()
        i = None
        j = None
        o = True
        self.assertEqual(s.flipEquiv(i,j), o)

    def test_three(self):
        s = Solution()
        i = None
        j = TreeNode(1)
        o = False
        self.assertEqual(s.flipEquiv(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)