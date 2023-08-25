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
    Given a binary tree, determine if it is height-balanced.

    A height balanced binary tree is a binary tree in which the height of the
    left subtree and right subtree of any node does not differ by more than 1
    and both the left and right subtree are also height balanced.
    https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
    '''
    def isBalanced_fails(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        depth = []
        # def dfs_wrong(node, d):
        #     if not node:
        #         return
        #     elif node.left or node.right:
        #         dfs(node.left, d+1)
        #         dfs(node.right, d+1)
        #     else:
        #         depth.append(d)
        def dfs(node, d):
            if not node:
                depth.append(d)
            else:
                dfs(node.left, d+1)
                dfs(node.right, d+1)
        dfs(root, 0)
        return max(depth) - min(depth) <= 1

    def isBalanced_fails2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        depth = []
        def dfs(node, d=0):
            if not node.left and not node.right:
                depth.append(d)
            if node.left:
                dfs(node.left, d+1)
            if node.right:
                dfs(node.right, d+1)
        dfs(root)
        return max(depth) - min(depth) <= 1

    # based on pair answer in geeks for geeks article
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0
            l = dfs(node.left)
            r = dfs(node.right)
            return l[0] and r[0] and abs(l[1] - r[1]) <= 1, max(l[1], r[1])
        return dfs(root)[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)