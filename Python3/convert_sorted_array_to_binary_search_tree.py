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
        return self.val == other.val and self.left == other.left and self.right == other.right
    def __repr__(self):
        return f'TreeNode(val:{repr(self.val)} left:{repr(self.left.val if self.left else None)} right:{repr(self.right.val if self.right else None)})'

class Solution:
    '''
    Given an integer array nums where the elements are sorted in 
    ascending order, convert it to a height-balanced binary search tree.

    A height-balanced binary tree is a binary tree in which the depth of
    the two subtrees of every node never differs by more than one.
    '''
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base case (empty array)
        if not nums:
            return None
        # find midpoint element
        midpoint = len(nums) // 2
        # recurse on elements to left of midpoint
        left = self.sortedArrayToBST(nums[:midpoint])
        # recurse on elements to right of midpoint
        right = self.sortedArrayToBST(nums[midpoint+1:])
        # return new TreeNode
        return TreeNode(nums[midpoint], left, right)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-10,-3,0,5,9]
        o = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
        self.assertEqual(s.sortedArrayToBST(i), o)

    def test_two(self):
        s = Solution()
        i = [1,3]
        o = TreeNode(3, TreeNode(1))
        self.assertEqual(s.sortedArrayToBST(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)