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
    Given the root node of a binary search tree and two integers low and
    high, return the sum of all nodes with a value in the inclusive
    range [low, high].
    '''
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        sum = 0
        if root.val >= low:
            sum += self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            sum += self.rangeSumBST(root.right, low, high)
        if root.val >= low and root.val <= high:
            sum += root.val
        return sum

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        t = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
        self.assertEqual(s.rangeSumBST(t, 7, 15), 32)

    def test_two(self):
        s = Solution()
        t = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))), TreeNode(15, TreeNode(13), 18))
        self.assertEqual(s.rangeSumBST(t, 6, 10), 23)

if __name__ == '__main__':
    unittest.main(verbosity=2)