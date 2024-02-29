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
    A binary tree is named Even-Odd if it meets the following conditions:
    * The root of the binary tree is at level index 0, its children are at level
      index 1, their children are at level index 2, etc.
    * For every even-indexed level, all nodes at the level have odd integer
      values in strictly increasing order (from left to right).
    * For every odd-indexed level, all nodes at the level have even integer
      values in strictly decreasing order (from left to right).
    
    Given the root of a binary tree, return true if the binary tree is Even-Odd,
    otherwise return false.
    '''
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        queue = [root]
        while queue:
            q = []
            if level % 2:
                v = 10**6+1
                for e in queue:
                    if e.val < v and e.val % 2 == 0:
                        v = e.val
                        if e.left:
                            q.append(e.left)
                        if e.right:
                            q.append(e.right)
                    else:
                        return False
            else:
                v = 0
                for e in queue:
                    if e.val > v and e.val % 2 == 1:
                        v = e.val
                        if e.left:
                            q.append(e.left)
                        if e.right:
                            q.append(e.right)
                    else:
                        return False
            queue = q
            level += 1
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(10, TreeNode(3, TreeNode(12), TreeNode(8))), TreeNode(4, TreeNode(7, TreeNode(6)), TreeNode(9, None, TreeNode(2))))
        o = True
        self.assertEqual(s.isEvenOddTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(4, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(7)))
        o = False
        self.assertEqual(s.isEvenOddTree(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(5, TreeNode(9, TreeNode(3), TreeNode(5)), TreeNode(1, TreeNode(7)))
        o = False
        self.assertEqual(s.isEvenOddTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)