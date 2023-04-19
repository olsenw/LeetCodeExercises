# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree.

    A ZigZag path for a binary ree is defined as follow:
    * Choose any node in the binary tree and a direction (right or left).
    * If the current direction is right, move to the right child of the current
      node, otherwise move to the left child.
    * Change the direction from right to left or from left to right.
    * Repeat the second and third steps until it is no longer possible to move
      in the tree.
    
    ZigZag length is defined as the number of nodes visited - 1. (A single node
    has a length of 0).

    Return the longest ZigZag path contained in that tree.
    '''
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        best = 0
        def dfs(node:Optional[TreeNode]) -> tuple[int,int]:
            if not node:
                return (-1,-1)
            a,b = dfs(node.left)
            x,y = dfs(node.right)
            a += 1
            y += 1
            nonlocal best
            best = max(best, max(a, y))
            return (y,a)
        dfs(root)
        return best

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(right=TreeNode(TreeNode(), TreeNode(TreeNode(right=TreeNode(right=TreeNode())), TreeNode())))
        o = 3
        self.assertEqual(s.longestZigZag(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(TreeNode(right=TreeNode(TreeNode(right=TreeNode()),TreeNode())),TreeNode())
        o = 4
        self.assertEqual(s.longestZigZag(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode()
        o = 0
        self.assertEqual(s.longestZigZag(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)