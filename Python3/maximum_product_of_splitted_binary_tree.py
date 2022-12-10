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
    Given the root of a binary tree, split the binary tree into two subtrees by
    removing one edge such that the product of the sums of the subtrees is
    maximized.
    
    Return the maximum product of the sums of the two subtrees. Since the answer
    may be too large, return it modulo 10^9 + 7.
    
    Note that maximized answer is found before the modulo operation.
    '''
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        m = 10**9 + 7
        def sumTree(node: Optional[TreeNode]):
            if not node:
                return 0
            node.val += sumTree(node.left) + sumTree(node.right)
            return node.val
        total = sumTree(root)
        def answer(node: Optional[TreeNode]):
            a = 0
            if node.left:
                a = max(a, answer(node.left), (total - node.left.val) * node.left.val)
            if node.right:
                a = max(a, answer(node.right), (total - node.right.val) * node.right.val)
            return a
        return answer(root) % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        o = 110
        self.assertEqual(s.maxProduct(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
        o = 90
        self.assertEqual(s.maxProduct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)