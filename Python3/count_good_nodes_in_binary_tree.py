# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given a binary tree root, a node X in the tree is named good if in
    the path from root to X there are no nodes with a value greater than
    X.

    Return the number of good nodes in the binary tree.
    '''
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        def dfs(node, large):
            nonlocal answer
            if large <= node.val:
                answer += 1
            if node.left:
                dfs(node.left, max(node.val, large))
            if node.right:
                dfs(node.right, max(node.val, large))
        dfs(root, root.val)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3,TreeNode(1, TreeNode(3)),TreeNode(4, TreeNode(1), TreeNode(5)))
        o = 4
        self.assertEqual(s.goodNodes(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(3,TreeNode(3,TreeNode(4),TreeNode(2)))
        o = 3
        self.assertEqual(s.goodNodes(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = 1
        self.assertEqual(s.goodNodes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)