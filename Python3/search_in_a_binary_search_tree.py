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
    Given the root of a binary search tree (BST) and an integer val.

    Find the node in the BST that the node's value equals val and return
    the subtree rooted with that node. If such a node does not exist,
    return null.
    '''
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        j = 2
        o = 2
        self.assertEqual(s.searchBST(i, j).val, o)

    def test_two(self):
        s = Solution()
        i = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        j = 5
        o = None
        self.assertEqual(s.searchBST(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)