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
    Given the root of a binary tree that consists of exactly 3 nodes: the root,
    its left child, and its right child.

    Return true if the values of the root is equal to the sum of the values of
    its two children, or false otherwise.
    '''
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(10, TreeNode(4), TreeNode(6))
        o = True
        self.assertEqual(s.checkTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(3), TreeNode(1))
        o = False
        self.assertEqual(s.checkTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)