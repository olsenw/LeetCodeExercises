# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque

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
    Given the root of a binary search tree, rearrange the tree to be
    in-order so that the leftmost node in the tree is now the root of
    the tree, and every node has no left child and only on right child.
    '''
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        head = dummy
        def recurse(root):
            nonlocal head
            # if not root:
            #     return
            if root.left:
                recurse(root.left)
            head.right = TreeNode(root.val)
            head = head.right
            if root.right:
                recurse(root.right)
        recurse(root)
        return dummy.right

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5,
                TreeNode(3,
                    TreeNode(2, TreeNode(1)),
                    TreeNode(4)),
                TreeNode(6,
                    None,
                    TreeNode(8, TreeNode(7), TreeNode(9))))
        o = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None, TreeNode(7, None, TreeNode(8, None, TreeNode(9)))))))))
        self.assertEqual(s.increasingBST(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(1), TreeNode(7))
        o = TreeNode(1, None, TreeNode(5, None, TreeNode(7)))
        self.assertEqual(s.increasingBST(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)