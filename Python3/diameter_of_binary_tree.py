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
    Given the root of a binary tree, return the length of the diameter of the
    tree.

    The diameter of a binary tree is the length of the longest path between any
    two nodes in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges
    between them.
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node):
            if not node:
                return -1
            a = 1 + dfs(node.left)
            b = 1 + dfs(node.right)
            nonlocal answer
            answer = max(answer, a + b)
            return max(a,b)
        dfs(root)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        o = 3
        self.assertEqual(s.diameterOfBinaryTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2))
        o = 1
        self.assertEqual(s.diameterOfBinaryTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)