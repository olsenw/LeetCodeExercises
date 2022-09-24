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
    Given the root of a binary tree and an iteger targetSum, return all
    root-to-leaf paths where the sum of the node values in the path equals
    targetSum. Each path should be returned as a list of the node values, not
    node references.

    A root-to-leaf path is path starting from the root and ending at any leaf
    node. A leaf is a node with no children.
    '''
    def pathSum_dfs_recursive(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        a = []
        p = []
        def dfs(node):
            nonlocal a
            nonlocal p
            p.append(node.val)
            if not node.left and not node.right and p and sum(p) == targetSum:
                a.append(list(p))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            p.pop()
        if root:
            dfs(root)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
        )
        j = 22
        o = [[5,4,11,2],[5,8,4,5]]
        self.assertEqual(s.pathSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        j = 5
        o = []
        self.assertEqual(s.pathSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2))
        j = 0
        o = []
        self.assertEqual(s.pathSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)