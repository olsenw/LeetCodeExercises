# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Given a binary tree with the following rules:
1) root.val == 0
2) If treeNode.val == x and treeNode.left != null, then
    treeNode.left.val = 2 * x + 1
3) If treeNode.val == x and treeNode.right != null, then
    treeNode.right.val = 2 * x + 2

Now the binary tree is contaminated, which means all treenode.val have been
changed to -1.

Implement the FindElements class:
'''
class FindElements:
    '''
    Initializes the object with contaminated binary tree and recovers it.
    '''
    def __init__(self, root: Optional[TreeNode]):
        s = set()
        def dfs(node, val):
            s.add(val)
            if node.left:
                dfs(node.left, 2 * val + 1)
            if node.right:
                dfs(node.right, 2 * val + 2)
        dfs(self.t, 0)
        self.s = s

    '''
    Returns true if the target value exists in the recovered binary tree.
    '''
    def find(self, target: int) -> bool:
        return target in self.s

class UnitTesting(unittest.TestCase):
    '''
    Tested online cause lazy
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)