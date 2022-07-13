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
    Given the root of a binary tree, return the level order traversal of
    its nodes' values. (ie from left to right, level by level)
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        level = [root] if root else []
        while level:
            nextLevel = []
            values = []
            for l in level:
                values.append(l.val)
                if l.left:
                    nextLevel.append(l.left)
                if l.right:
                    nextLevel.append(l.right)
            ans.append(values)
            level = nextLevel
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        o = [[3],[9,20],[15,7]]
        self.assertEqual(s.levelOrder(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        o = [[1]]
        self.assertEqual(s.levelOrder(i), o)

    def test_three(self):
        s = Solution()
        i = None
        o = []
        self.assertEqual(s.levelOrder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)