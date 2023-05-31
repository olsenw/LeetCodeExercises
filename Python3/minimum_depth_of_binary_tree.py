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
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the
    root node down to the nearest leaf node.

    A leaf is a node with no children.
    '''
    def minDepth(self, root: Optional[TreeNode]) -> int:
        answer = 10**5
        def dfs(node: TreeNode, depth=1):
            nonlocal answer
            if not node.left and not node.right:
                answer = min(answer, depth)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        if root:
            dfs(root)
            return answer
        return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = None
        o = 0
        self.assertEqual(s.minDepth(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        o = 1
        self.assertEqual(s.minDepth(i), o)

    '''
    Rest of test cases are on LeetCode
    '''

if __name__ == '__main__':
    unittest.main(verbosity=2)