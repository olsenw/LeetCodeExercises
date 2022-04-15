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
        if type(other) == TreeNode:
            return self.val == other.val and self.left == other.left and self.right == other.right
        return False

class Solution:
    '''
    Given the root of a binary search tree and the lowest and highest
    boundaries as low and high, trim the tree so that all its elements
    lie in [low, high]. Trimming the tree should not change the relative
    structure of the elements that will remain in the tree (ie any
    node's descendants should remain descendants). It can be proven that
    there is a unique answer.

    Return the root of the trimmed binary search tree. Note that the
    root may change depending on the given bounds.
    '''
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1,TreeNode(0),TreeNode(2))
        j = 1
        k = 2
        o = TreeNode(1,None,TreeNode(2))
        self.assertEqual(s.trimBST(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))
        j = 1
        k = 3
        o = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(s.trimBST(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)