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
    Given the root of a binary tree with n nodes. Each node is uniquely assigned
    a value from 1 to n. Also given an integer startValue representing the value
    of the start node s, and a different destValue representing the value of the
    destination node t.

    Find the shortest path starting from node s and ending at node t. Generate
    step-by-step directions of such paths as a string consisting of only the
    uppercase letters 'L', 'R' and 'U'. Each letter indicates a specific
    direction:
    * 'L' means to go from a node to its left child node.
    * 'R' means to go from a node to its right child node.
    * 'U' means to go from a node to its parent node.

    Return the step by step directions of the shortest path from node s to node
    t.
    '''
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        a,b = [], []
        def dfs(node:Optional[TreeNode], target, stack):
            if not node:
                return
            if node.val == target:
                return True
            stack.append('L')
            if dfs(node.left, target, stack):
                return True
            stack.pop()
            stack.append('R')
            if dfs(node.right, target, stack):
                return True
            stack.pop()
            return False
        dfs(root, startValue, a)
        dfs(root, destValue, b)
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1
        return 'U'*(len(a)-i) + ''.join(b[i:])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))
        j = 3
        k = 6
        o = "UURL"
        self.assertEqual(s.getDirections(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(2, TreeNode(1))
        j = 2
        k = 1
        o = "L"
        self.assertEqual(s.getDirections(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(3, None, TreeNode(4))), TreeNode(5, None, TreeNode(6, TreeNode(7))))
        j = 7
        k = 4
        o = "UUULLR"
        self.assertEqual(s.getDirections(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)