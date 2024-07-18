# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree and an integer distance. A pair of two
    different leaf nodes of a binary tree is said to be good if the length of
    shortest path between them is less than or equal to distance.

    Return the number of good leaf node pairs in the tree.
    '''
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf = []
        def dfs(node:TreeNode, parent:Optional[TreeNode]):
            if node.left is None and node.right is None:
                leaf.append(node)
            node.parent = parent
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        dfs(root, None)
        answer = 0
        def check(node:TreeNode, prev:Optional[TreeNode], depth:int):
            nonlocal answer
            if depth > distance:
                return
            if node is not prev and node.left is None and node.right is None:
                answer += 1
            if node.left and node.left is not prev:
                check(node.left, node, depth+1)
            if node.right and node.right is not prev:
                check(node.right, node, depth+1)
            if node.parent and node.parent is not prev:
                check(node.parent, node, depth+1)
        for node in leaf:
            check(node, node, 0)
        return answer // 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        j = 3
        o = 1
        self.assertEqual(s.countPairs(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        j = 3
        o = 2
        self.assertEqual(s.countPairs(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)