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
    Given the root of a binary tree, construct a string consisting of
    parenthesis and integers from a binary tree with the preorder
    traversal way, and return it.

    Omit all the empty parenthesis pairs that do not affect the
    one-to-one mapping relationship between the string and the original
    binary tree.
    '''
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        a = str(root.val)
        b = self.tree2str(root.left)
        c = self.tree2str(root.right)
        return a + (f'({b})' if b or c else "") + (f'({c})' if c else "")

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        o = "1(2(4))(3)"
        self.assertEqual(s.tree2str(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        o = "1(2()(4))(3)"
        self.assertEqual(s.tree2str(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)