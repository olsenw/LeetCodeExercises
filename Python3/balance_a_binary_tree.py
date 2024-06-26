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
    Given the root of a binary search tree, return a balanced binary search tree
    with the same node values. If there is more than one answer return any of
    them.

    A binary search tree is balanced if the depth of the two subtrees of every
    node never differs by more than 1.
    '''
    def balanceBST(self, root: TreeNode) -> TreeNode:
        t = []
        def p(node: TreeNode):
            if not node:
                return
            p(node.left)
            t.append(node.val)
            p(node.right)
            return
        p(root)
        def build(i:int, j:int):
            if i > j:
                return None
            k = i + (j - i) // 2
            return TreeNode(t[k], build(i, k-1), build(k+1,j))
        return build(0, len(t)-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)