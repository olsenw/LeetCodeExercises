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
    Given the root of a binary tree and an integer targetSum, return true if the
    tree has a root-to-leaf path such that adding up all the values along the
    path equals targetSum.
    
    A leaf is a node with no children.
    '''
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        if root.left and self.hasPathSum(root.left, targetSum - root.val):
            return True
        if root.right and self.hasPathSum(root.right, targetSum - root.val):
            return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
        j = 22
        o = True
        self.assertEqual(s.hasPathSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        j = 5
        o = False
        self.assertEqual(s.hasPathSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = None
        j = 0
        o = False
        self.assertEqual(s.hasPathSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)