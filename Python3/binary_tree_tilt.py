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
    Find the total tilt of the binary tree

    Tilt is the abs(sum of left subtree - sum of right subtree)
    '''
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.helper(root)[1]

    # returns a tuple of (sum of subtree, sum tilt of subtree)
    def helper(self, root: Optional[TreeNode]) -> (int, int):
        if root is None:
            return (0,0)
        left = self.helper(root.left)
        right = self.helper(root.right)
        tilt = abs(left[0] - right[0])
        return (root.val + left[0] + right[0], tilt + left[1] + right[1])

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        t = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(s.findTilt(t), 1)

    def test_two(self):
        s = Solution()
        t = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
        self.assertEqual(s.findTilt(t), 15)

    def test_three(self):
        s = Solution()
        t = TreeNode(21, TreeNode(7, TreeNode(1, TreeNode(3), TreeNode(3)), TreeNode(1)), TreeNode(14, TreeNode(2), TreeNode(2)))
        self.assertEqual(s.findTilt(t), 9)

if __name__ == '__main__':
    unittest.main(verbosity=2)