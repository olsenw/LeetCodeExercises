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
        return type(other) == TreeNode and self.val == other.val \
            and self.left == other.left and self.right == other.right

class Solution:
    '''
    Given the root of a Binary Search Tree (BST), convert it to a
    Greater Tree such that every key of the original BST is changed to
    the original key plus the sum of all keys greater than the original
    key in BST.
    '''
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0
        def recurse(root: Optional[TreeNode]):
            nonlocal s
            if not root:
                return
            if root.right:
                recurse(root.right)
            s += root.val
            root.val = s
            if root.left:
                recurse(root.left)
            return
        recurse(root)
        return root

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(4,
                TreeNode(1, TreeNode(0),TreeNode(2, None, TreeNode(3))),
                TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
        o = TreeNode(30,
                TreeNode(36, TreeNode(36), TreeNode(35, None, TreeNode(33))),
                TreeNode(21, TreeNode(26), TreeNode(15, None, TreeNode(8))))
        self.assertEqual(s.convertBST(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(0, None, TreeNode(1))
        o = TreeNode(1, None, TreeNode(1))
        self.assertEqual(s.convertBST(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)