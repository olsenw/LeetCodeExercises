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
    Given the root of a binary tree, return the number of nodes where the value
    of the node is equal to the average of the values in its subtree.

    Note:
    * The average of n elements is the sum of the n elements divided by n and
      rounded down to the nearest integer.
    * A subtree of root is a tree consisting of root and all of its descendants.
    '''
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node):
            nonlocal answer
            if not node:
                return 0,0
            a,b = dfs(node.left)
            c,d = dfs(node.right)
            if (node.val + a + c) // (b + d + 1) == node.val:
                answer += 1
            return node.val + a + c, b + d + 1
        dfs(root)
        return answer

class UnitTesting(unittest.TestCase):
    # tested online
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)