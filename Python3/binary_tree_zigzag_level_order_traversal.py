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
    Given the root of a binary tree, return the zigzag level order traversal of
    its nodes' values. (ie from left to right, then right to left for the next
    level and alternate between). 
    '''
    # incorrect
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zig = []
        zag = True
        a = [root]
        while a:
            if zag:
                zig.append(i.val for i in a)
            else:
                zig.append(i.val for i in a[::-1])
            b = []
            for i in a:
                if i.left:
                    b.append(i.left)
                if i.right:
                    b.append(i.right)
            a = b
            zag = not zag
        return zig

class UnitTesting(unittest.TestCase):
    '''
    tested online
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)