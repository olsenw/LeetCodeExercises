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
    Given the root of a binary tree and two integers val and depth, add a row of
    nodes with value val at the given depth.
    
    Note that the root node is at depth 1.
    
    The adding rule is:
    * Given the integer depth, for each not null tree node cur at the depth
      depth - 1, create two tree nodes with value val as cur's left subtree root
      and right subtree root.
    * cur's original left subtree should be the left subtree of the new left
      subtree root.
    * cur's original right subtree should be the right subtree of the new right
      subtree root.
    * If depth == 1 that means there is no depth depth - 1 at all, then create a
      tree node with value val as the new root of the whole original tree, and
      the original tree is the new root's left subtree.
    '''
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        def idfs(node, cd):
            if cd == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            if node.left:
                idfs(node.left, cd + 1)
            if node.right:
                idfs(node.right, cd + 1)
        idfs(root, 1)
        return root

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
        j = 1
        k = 2
        o = TreeNode(4, TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(1))), TreeNode(1, None, (TreeNode(6, TreeNode(5)))))
        self.assertEqual(s.addOneRow(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
        j = 1
        k = 3
        o = TreeNode(4, TreeNode(2, TreeNode(1, TreeNode(3)), TreeNode(1, None, TreeNode(1))))
        self.assertEqual(s.addOneRow(i,j,k), o)
    
    def test_three(self):
        s = Solution()
        i = TreeNode(2)
        j = 1
        k = 1
        o = TreeNode(1, TreeNode(2))
        self.assertEqual(s.addOneRow(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)