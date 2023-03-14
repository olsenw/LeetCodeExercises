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
    Given the root of a binary tree, determine if it is a complete binary tree.

    In a complete binary tree, every level, except possibly the last, is
    completely filled, and all nodes in the last level are as far left as
    possible. It is possible to have 1 to 2^h inclusive, nodes at the last level
    h.
    '''
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        layer = [root]
        while layer:
            advance = []
            for i,l in enumerate(layer):
                if not l:
                    return not any(layer[i+1:]) and not any(advance)
                advance.append(l.left)
                advance.append(l.right)
            layer = advance
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6))
        )
        o = True
        self.assertEqual(s.isCompleteTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, None, TreeNode(7))
        )
        o = False
        self.assertEqual(s.isCompleteTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)