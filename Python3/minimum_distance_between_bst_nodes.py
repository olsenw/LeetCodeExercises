# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
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
    Given the root of a Binary Search Tree (BST), return the minimum difference
    between the values of any two different nodes in the tree.
    '''
    # incorrect - this finds two smallest values, need to find two closest values
    def minDiffInBST_fail(self, root: Optional[TreeNode]) -> int:
        h = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            if len(h) < 2:
                heapq.heappush(h, -node.val)
            else:
                heapq.heappushpop(h, -node.val)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return (-h[0]) - (-h[1])

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return min(values[i] - values[i-1] for i in range(1, len(values)))

class UnitTesting(unittest.TestCase):
    '''Tested online'''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)