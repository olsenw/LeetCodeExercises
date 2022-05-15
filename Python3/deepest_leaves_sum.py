# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree, return the sum of values of its
    deepest leaves.
    '''
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depth = 0
        accum = 0
        def r(n, d):
            nonlocal depth
            nonlocal accum
            if d > depth:
                depth = d
                accum = 0
            if d == depth:
                accum += n.val
            if n.left:
                r(n.left, d + 1)
            if n.right:
                r(n.right, d + 1)
        r(root, 1)
        return accum

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
        o = 15
        self.assertEqual(s.deepestLeavesSum(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(6,
                TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))),
                TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
        o = 19
        self.assertEqual(s.deepestLeavesSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)