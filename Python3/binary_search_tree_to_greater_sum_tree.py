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
    Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
    such that every key of the original BST is changed to the original key plus
    the sum of all keys greater than the original key in BST.
    '''
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def post(node:TreeNode, running:int) -> int:
            if not node:
                return running
            node.val += post(node.right, running)
            return post(node.left, node.val)
        post(root, 0)
        return root

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.bstToGst(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(0, None, TreeNode(1))
        o = TreeNode(1, None, TreeNode(1))
        self.assertEqual(s.bstToGst(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)