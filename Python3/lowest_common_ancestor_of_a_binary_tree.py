# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right

class Solution:
    '''
    Given a binary tree, find the lowest common ancestor (LCA) of two
    given nodes in the tree.

    According to the definition of LCA on Wikipedia: "The lowest common
    ancestor is defined between two nodes p and q as the lowest node in
    T that has both p and q as descendants (where we allow a node to be
    a descendant of itself)."
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(head, target, path):
            path.append(head)
            if target.val == head.val:
                return path
            if head.left and dfs(head.left, target, path):
                return path
            if head.right and dfs(head.right, target, path):
                return path
            path.pop()
            return None
        a, b = [], []
        dfs(root, p, a)
        dfs(root, q, b)
        ans = None
        for i,j in zip(a,b):
            if i.val != j.val:
                break
            ans = i
        return ans

class UnitTesting(unittest.TestCase):
    def test_three(self):
        s = Solution()
        two = TreeNode(2)
        one = TreeNode(1)
        one.left = two
        self.assertEqual(s.lowestCommonAncestor(one,one,two), one)

if __name__ == '__main__':
    unittest.main(verbosity=2)