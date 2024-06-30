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
    Given a non-empty special binary tree consisting of nodes with the
    non-negative value, where each node in this tree has exactly two or zero
    sub-nodes. If the node has two sub-nodes, then this node's value is the
    smaller value among its its two sub-nodes. More formally, the property
    root.val = min(root.left.val, root.right.val) always holds.

    Given such a binary tree, output the second minimum value in the set made of
    all the nodes' value in the whole tree.

    If no such second minimum value exists, output -1 instead.
    '''
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node:Optional[TreeNode], target:int) -> int:
            if node.val > target:
                return node.val
            left, right = node.val,node.val
            if node.left:
                left = dfs(node.left, target)
            if node.right:
                right = dfs(node.right, target)
            if target < left or target < right:
                if target < left < right:
                    return left
                if target < right < left:
                    return right
                if target < left:
                    return left
                if target < right:
                    return right
            return node.val
        a = dfs(root, root.val)
        return -1 if root.val == a else a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
        o = 5
        self.assertEqual(s.findSecondMinimumValue(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(2, TreeNode(2), TreeNode(2))
        o = -1
        self.assertEqual(s.findSecondMinimumValue(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)