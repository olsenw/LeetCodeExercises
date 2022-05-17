# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Given two binary trees original and cloned and given a reference to
    a nod target in the original tree.

    The cloned tree is a copy of the original tree.

    Return a reference to the same node in the cloned tree.

    Note: do not change either of the two trees or the target node and
    the answer must be a reference to a node in the cloned tree.
    '''
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is target:
            return cloned
        r = None
        if original.left:
            r = self.getTargetCopy(original.left, cloned.left, target)
        if r:
            return r
        if original.right:
            r = self.getTargetCopy(original.right, cloned.right, target)
        return r
    
    '''
    Follow up: Could this problem be solved if repeated value in the
    same tree are allowed?

    Yes, above code already does that. It searches the original tree for
    a node with the same memory address (instead of value) as target.
    '''

class UnitTesting(unittest.TestCase):
    '''
    Did testing on Leetcode because I did not want to copy trees over.
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)