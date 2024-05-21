# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
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
    Given the root of a binary tree, return the bottom up level order traversal
    of its nodes' values. (ie, from left to right, level by level from leaf to 
    root).
    '''
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def dfs(node, depth):
            if node is None:
                return
            d[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return [d[i] for i in range(len(d)-1, -1, -1)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        o = [[15,7],[9,20],[3]]
        self.assertEqual(s.levelOrderBottom(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        o = [[1]]
        self.assertEqual(s.levelOrderBottom(i), o)

    def test_two(self):
        s = Solution()
        i = None
        o = []
        self.assertEqual(s.levelOrderBottom(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)