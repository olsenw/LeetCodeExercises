# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
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
    Given the root of a binary tree, check whether it is a mirror of itself (ie
    symmetric around its center).
    '''
    # horrible, but passes
    def isSymmetric_yuck(self, root: Optional[TreeNode]) -> bool:
        layer = [root]
        while layer:
            below = []
            check = []
            for l in layer:
                if l:
                    check.append(l.val)
                    below.append(l.left)
                    below.append(l.right)
                else:
                    check.append(None)
                    below.append(None)
                    below.append(None)
            if all(c == None for c in check):
                break
            if check != check[::-1]:
                return False
            layer = below
        return True

    # solution based on discussion post by GeekErrra
    # https://leetcode.com/problems/symmetric-tree/solutions/3290132/python-java-c-efficient-solution/
    # recursive solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and isMirror(a.right, b.left) and isMirror(a.left, b.right)
        return isMirror(root, root)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        o = False
        self.assertEqual(s.isSymmetric(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        o = True
        self.assertEqual(s.isSymmetric(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = True
        self.assertEqual(s.isSymmetric(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)