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
    Given the root of a binary tree, return the leftmost value in the last row
    of the tree.
    '''
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            a,b = node.val, depth
            c,d = 0,0
            if node.left:
                c,d = dfs(node.left, depth+1)
            if d > b:
                a,b = c,d
            if node.right:
                c,d = dfs(node.right, depth+1)
            if d > b:
                a,b = c,d
            return a,b
        return dfs(root, 1)[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(2, TreeNode(1), TreeNode(3))
        o = 1
        self.assertEqual(s.findBottomLeftValue(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
        o = 7
        self.assertEqual(s.findBottomLeftValue(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)