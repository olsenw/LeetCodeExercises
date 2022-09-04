# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

from sortedcontainers import SortedDict, SortedList

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree, calculate the vertical order
    traversal of the binary tree.

    For each node at position (row, col), its left and right children
    will be at positions (row + 1, col - 1) and (row + 1, col + 1)
    respectively. The root of the tree is at (0,0).

    The vertical order traversal of a binary tree is a list of
    top-to-bottom orderings for each column index starting from the
    leftmost column and ending on the rightmost column. There may be
    multiple nodes in the same row and same column. In such a case, sort
    these nodes by their values.

    Return the vertical order traversal of the binary tree.
    '''
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = SortedDict()
        def dfs(node, row, column):
            nonlocal values
            if column in values:
                values[column].add((row, node.val))
            else:
                values[column] = SortedList([(row, node.val)])
            if node.left:
                dfs(node.left, row + 1, column - 1)
            if node.right:
                dfs(node.right, row + 1, column + 1)
        dfs(root, 0, 0)
        return [[b for a,b in values[v]] for v in values]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        o = [[9],[3,15],[20],[7]]
        self.assertEqual(s.verticalTraversal(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        o = [[4],[2],[1,5,6],[3],[7]]
        self.assertEqual(s.verticalTraversal(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(5), TreeNode(7)))
        o = [[4],[2],[1,5,6],[3],[7]]
        self.assertEqual(s.verticalTraversal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)