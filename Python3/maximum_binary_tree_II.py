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
    A maximum tree is a tree where every nodes has a value greater than any 
    other value in its subtree.

    Given the root of a maximum binary tree and an integer val.

    The given tree was constructed from a list a (root = Construct(a))
    recursively with the following Construct(a) routine:
    * If a is empty, return null
    * Otherwise, let a[i] be the largest element of a. Create a root node with
      the value a[i].
    * The left child of root will be Construct(a[0], a[1], ..., a[i-1]).
    * The right child of root will be
      Construct(a[i+1], a[i+2], ..., a[a.len - 1]).
    * Return root.

    Note that a is not given directly, only a root node root = Construct(a).

    Suppose b is a copy of a with the value val appended to it. It is guaranteed
    that b has unique values.

    Return Construct(b).
    '''
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def construct(values:list[int]) -> Optional[TreeNode]:
            if len(values) == 0:
                return None
            i = 0
            x = values[0]
            for j,y in enumerate(values):
                if y > x:
                    i,x = j,y
            left = construct(values[:i])
            right = construct(values[i+1:])
            return TreeNode(x, left, right)
        def destruct(node:Optional[TreeNode]) -> list[int]:
            if node is None:
                return []
            left = destruct(node.left)
            right = destruct(node.right)
            return left + [node.val] + right
        values = destruct(root)
        values.append(val)
        answer = construct(values)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(4, TreeNode(1), TreeNode(3, TreeNode(2)))
        j = 5
        o = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(3, TreeNode(2))))
        self.assertEqual(s.insertIntoMaxTree(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(4))
        j = 3
        o = TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(4, None, TreeNode(3)))
        self.assertEqual(s.insertIntoMaxTree(i,j), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(3))
        j = 4
        o = TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(4, TreeNode(3)))
        self.assertEqual(s.insertIntoMaxTree(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)