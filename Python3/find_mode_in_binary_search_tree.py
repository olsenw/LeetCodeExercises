# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
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
    Given the root of a binary search tree (BST) with duplicates, return all the
    modes(s) (ie, the most frequently occurred element) in it.

    If the tree has more than one mode, return them in any order.

    Assume a BST is defined as follows:
    * The left subtree of a node contains only nodes with keys less than or
      equal to the node's key.
    * The right subtree of a node contains only nodes with keys greater than or
      equal to the node's key.
    * Both the left and right subtrees must also be binary search trees.
    '''
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c = Counter()
        def dfs(node):
            if not node:
                return
            c[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        a = c.most_common()
        return [i for i,j in a if j == a[0][1]]

class UnitTesting(unittest.TestCase):
    '''
    Tested online
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)