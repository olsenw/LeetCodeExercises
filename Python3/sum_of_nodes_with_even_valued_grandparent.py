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
    Given the root of a binary tree, return the sum of values of nodes with an
    even-valued grandparent. If there are no nodes with an even-valued
    grandparent return 0.

    A grandparent of a node is the parent of its parent if it exists.
    '''
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node:Optional[TreeNode], parent:Optional[TreeNode], grand:Optional[TreeNode]) -> int:
            if node is None:
                return 0
            answer = 0
            if grand and grand.val % 2 == 0:
                answer += node.val
            answer += dfs(node.left, node, parent)
            answer += dfs(node.right, node, parent)
            return answer
        return dfs(root, None, None)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, TreeNode(5))))
        o = 18
        self.assertEqual(s.sumEvenGrandparent(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        o = 0
        self.assertEqual(s.sumEvenGrandparent(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)