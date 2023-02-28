# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
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
    def __eq__(self, __o: 'TreeNode') -> bool:
        return self.val == __o.val and self.left == __o.left and self.right == __o.right

class Solution:
    '''
    Given the root of a binary tree, return all duplicate subtrees.

    For each kind of duplicate subtrees, it is only required to return the root
    node of any one of them.

    Two trees are duplicates if they have the same structure with the same node
    values.
    '''
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        c: Dict[str, List[TreeNode, int]] = dict()
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return " "
            l = dfs(node.left)
            r = dfs(node.right)
            t = str(node.val) + ',' + l + ',' + r
            if t in c:
                c[t][1] += 1
            else:
                c[t] = [node, 1]
            return t
        dfs(root)
        a = [c[i][0] for i in c if c[i][1] > 1]
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(2, TreeNode(1), TreeNode(1))
        o = [TreeNode(1)]
        self.assertEqual(s.findDuplicateSubtrees(i), o)

    # fails here but passes online
    def test_two(self):
        s = Solution()
        i = TreeNode(2,TreeNode(2, TreeNode(3)),TreeNode(2, TreeNode(3)))
        o = [TreeNode(2, TreeNode(3)), TreeNode(3)]
        self.assertEqual(s.findDuplicateSubtrees(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)