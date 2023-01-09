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
    Given the root of a binary tree, return the preorder traversal of its nodes'
    values.
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        a = [root.val]
        b = self.preorderTraversal(root.left)
        c = self.preorderTraversal(root.right)
        return a + b + c

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        o = [1,2,3]
        self.assertEqual(s.preorderTraversal(i), o)

    def test_two(self):
        s = Solution()
        i = None
        o = []
        self.assertEqual(s.preorderTraversal(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = [1]
        self.assertEqual(s.preorderTraversal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)