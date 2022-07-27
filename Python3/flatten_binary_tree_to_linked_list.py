# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right

class Solution:
    '''
    Given the root of a binary tree flatten the tree into a "linked
    list":
    * The "linked list" should use the same TreeNode class where the
      right child pointer points to the next node in the list and the
      left child pointer is always null.
    * The "linked list" should be in the same order as a pre-order
      traversal of the binary tree.
    '''
    def flatten(self, root: Optional[TreeNode]) -> None:
        flat = []
        def porder(head):
            flat.append(head)
            if head.left:
                porder(head.left)
            if head.right:
                porder(head.right)
        if root:
            porder(root)
        for i in range(len(flat) - 1):
            flat[i].left = None
            flat[i].right = flat[i+1]

    '''
    Did not do the O(1) space follow up.
    Could do this by making use of the left pointer to keep track of 
    where to go next.
    '''

class UnitTesting(unittest.TestCase):
    '''
    Did testing only on Leetcode
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)