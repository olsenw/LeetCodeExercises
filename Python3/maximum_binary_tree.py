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
    Given an integer array nums with no duplicates. A maximum binary tree can be
    built recursively from nums using the following algorithm:

    1. Create a root node whose value is the maximum value in nums.
    2. Recursively build the left subtree on the subarray prefix to the left and
       of the maximum value.
    3. Recursively build the right subtree on the subarray suffix to the right
       of the maximum value.
    
    Return the maximum binary tree built from nums.
    '''
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        m = 0
        n = 0
        for i in range(len(nums)):
            if m < nums[i]:
                m = nums[i]
                n = i
        if len(nums) == 1:
            return TreeNode(m)
        if len(nums) == 0:
            return None
        a = TreeNode(m, self.constructMaximumBinaryTree(nums[:n]), self.constructMaximumBinaryTree(nums[n+1:]))
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)