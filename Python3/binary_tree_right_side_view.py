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

class Solution:
    '''
    Given the root of a binary tree, imagine a viewer standing on the
    right side of the tree, return the values that viewer can see
    ordered from top to bottom.
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = [root] if root else []
        ans = []
        while level:
            n = []
            for l in level:
                if l.left:
                    n.append(l.left)
                if l.right:
                    n.append(l.right)
            ans.append(level[-1].val)
            level = n
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        o = [1,3,4]
        self.assertEqual(s.rightSideView(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(3))
        o = [1,3]
        self.assertEqual(s.rightSideView(i), o)

    def test_three(self):
        s = Solution()
        i = None
        o = []
        self.assertEqual(s.rightSideView(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)