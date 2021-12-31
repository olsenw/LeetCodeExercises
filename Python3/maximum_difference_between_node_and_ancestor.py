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
    Given the root of a binary tree, find the maximum value v for which
    there exist different nodes a and b where v = abs(a.val - b.val)
    and a is an ancestor of b.

    A node a is an ancestor of b if either: any child of a is equal to b
    or any child of a is an ancestor of b.
    '''
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recurse(root: Optional[TreeNode], small: int, large: int) -> int:
            # hit a leaf node return the difference of smallest and 
            # largest node found this path
            if root is None:
                return large - small
            # update smallest/largest node so far
            small = min(root.val, small)
            large = max(root.val, large)
            # recurse on children nodes
            left = recurse(root.left, small, large)
            right = recurse(root.right, small, large)
            # bounce up best answer so far
            return max(left, right)
        # call recursive algorithm with initial parameters
        return recurse(root, 10**5+1, 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
        o = 7
        self.assertEqual(s.maxAncestorDiff(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))
        o = 3
        self.assertEqual(s.maxAncestorDiff(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(10, TreeNode(5, TreeNode(9), TreeNode(2)))
        o = 8
        self.assertEqual(s.maxAncestorDiff(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)