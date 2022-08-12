# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a binary search tree (BST), find the lowest common ancestor
    (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: "The lowest common
    ancestor is defined between two nodes p and q as the lowest node in
    T that has both p and q as descendants (where we allow a node to be
    a descendant of itself)."
    '''
    def lowestCommonAncestor_passes(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        elif root.val <= q.val and root.val <= p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val >= q.val and root.val >= p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

class UnitTesting(unittest.TestCase):
    '''
    Passed on Leetcode when ran from phone
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)