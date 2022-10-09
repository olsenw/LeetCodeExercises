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
    Given the root of a Binary Search Tree and a target number k, return true if
    there exist two elements in the BST such that their sum is equal to the
    given target.
    '''
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d = set()
        def dfs(node):
            if k - node.val in d:
                return True
            d.add(node.val)
            if node.left and dfs(node.left):
                return True
            if node.right and dfs(node.right):
                return True
            return False
        return dfs(root)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
        j = 9
        o = True
        self.assertEqual(s.findTarget(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
        j = 28
        o = False
        self.assertEqual(s.findTarget(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)