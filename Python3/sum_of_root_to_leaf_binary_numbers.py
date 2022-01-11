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
    Given the root of a binary tree where each node has a value of 0 or 
    1. Each root-to-leaf path represents a binary number starting with 
    the most significant bit.

    Example: path 0->1->1->0->1 represents binary 01101 which is 13.

    For all leaves in the tree consider the numbers represented by the 
    path from root to that leaf. Return the sum of these numbers.
    '''
    # O(n) time
    # O(h) space where h is height of binary tree
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        answer = 0
        # DFS Pre Order traversal
        def recurse(root: Optional[TreeNode], a: int) -> None:
            a += root.val
            # base case
            if not root.left and not root.right:
                nonlocal answer
                answer += a
            if root.left:
                recurse(root.left, a << 1)
            if root.right:
                recurse(root.right, a << 1)
        recurse(root, 0)
        return answer
    
    # there is an alternate solution using the Morris Algorithm that can
    # do this in O(1) space... but it breaks the links in the tree.
    # Youtube link to explain the algorithm:
    # https://www.youtube.com/watch?v=wGXB9OWhPTg

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))
        o = 22
        self.assertEqual(s.sumRootToLeaf(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(0)
        o = 0
        self.assertEqual(s.sumRootToLeaf(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = 1
        self.assertEqual(s.sumRootToLeaf(i), o)

    def test_four(self):
        s = Solution()
        i = TreeNode(0, TreeNode(0), TreeNode(1))
        o = 1
        self.assertEqual(s.sumRootToLeaf(i), o)

    def test_five(self):
        s = Solution()
        i = TreeNode(1, TreeNode(0), TreeNode(1, TreeNode(1)))
        o = 9
        self.assertEqual(s.sumRootToLeaf(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)