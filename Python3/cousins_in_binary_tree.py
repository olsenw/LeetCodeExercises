# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree with unique values an the values of two
    different nodes of the tree x and y, return true if the nodes corresponding
    to the value x and y in the tree are cousins, or false otherwise.

    Two nodes of a binary tree are cousins if they have the same depth with
    different parents.

    Note that in a binary tree, the rood note is at the depth 0, and children of
    each depth k node are at the depth k + 1.
    '''
    # does not account for depth
    def isCousins_fails(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def findParent(target: int, node: Optional[TreeNode], parent: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            if node.val == target:
                return parent
            left = findParent(target, node.left, node)
            if left is not None:
                return left
            return findParent(target, node.right, node)
        a,b = findParent(x, root, None), findParent(y, root, None)
        return a.val != b.val

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def find(target:int, depth:int, root:Optional[TreeNode], parent:Optional[TreeNode]) -> Optional[Tuple[int, TreeNode]]:
            if root is None:
                return None
            if root.val == target:
                return (depth, parent)
            left = find(target, depth+1, root.left, root)
            if left is not None:
                return left
            return find(target, depth+1, root.right, root)
        a,b = find(x, 0, root, None)
        x,y = find(y, 0, root, None)
        return a == x and b.val != y.val

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        j = 4
        k = 3
        o = False
        self.assertEqual(s.isCousins(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
        j = 5
        k = 4
        o = True
        self.assertEqual(s.isCousins(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        j = 2
        k = 3
        o = False
        self.assertEqual(s.isCousins(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)