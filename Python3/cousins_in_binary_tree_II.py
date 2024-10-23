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
    def __eq__(self, value: object) -> bool:
        return self.val == value.val and self.left == value.left and self.right == value.right

class Solution:
    '''
    Given the root of a binary tree, replace the value of each node in the tree
    with the sum of all it's cousins values.

    Two nodes of a binary tree are cousins if they have the same depth with
    different parents.

    Return the root of the modified tree.

    Note that the depth of a node is the number edges in the path from the root
    node to it.
    '''
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = []
        def dfs(node: TreeNode, depth: int):
            if len(sums) < depth:
                sums.append(0)
            sums[depth - 1] += node.val
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        def fix(node: TreeNode, sibling: int, depth: int):
            node.val = sums[depth - 1] - node.val - sibling
            a = node.left.val if node.left else 0
            b = node.right.val if node.right else 0
            if node.left:
                fix(node.left, b, depth + 1)
            if node.right:
                fix(node.right, a, depth + 1)
        dfs(root, 1)
        fix(root, 0, 1)
        return root

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, None, TreeNode(7)))
        o = TreeNode(0, TreeNode(0, TreeNode(7), TreeNode(7)), TreeNode(0, None, TreeNode(11)))
        self.assertEqual(s.replaceValueInTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(3, TreeNode(1), TreeNode(2))
        o = TreeNode(0, TreeNode(0), TreeNode(0))
        self.assertEqual(s.replaceValueInTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)