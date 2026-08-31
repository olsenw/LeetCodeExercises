# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a complete binary tree.

    A node x is called dominant if its value is equal to the maximum value among
    all nodes in the subtree rooted at x.

    Return the number of dominant nodes in the tree.
    '''
    def countDominantNodes(self, root: TreeNode | None) -> int:
        # maximum value, number of dominate nodes
        def dominant(root:TreeNode) -> Tuple[int,int]:
            # if root.left == None and root.right == None:
            #     return (root.val, 1)
            if root is None:
                return (0,0)
            a,b = dominant(root.left)
            x,y = dominant(root.right)
            return (max(a,x,root.val), b + y + 1 if root.val >= a and root.val >= x else b + y)
        return dominant(root)[1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,3,8,2,4,7,1]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,1,2]
        o = 4
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)