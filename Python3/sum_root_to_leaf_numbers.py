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
    Given the root of a binary tree containing digits from 0 to 9 only.

    Each root-to-leaf path in the tree represents a number.

    Return the total sum of all root-to-leaf numbers. Test cases are generated
    so that the answer will fit in a 32-bit integer.

    A leaf node is a node with no children.
    '''
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def r(node:Optional[TreeNode], current:int):
            nonlocal answer
            current *= 10
            current += node.val
            if not node.left and not node.right:
                answer += current
                return
            if node.left:
                r(node.left, current)
            if node.right:
                r(node.right, current)
        r(root,0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        o = 25
        self.assertEqual(s.sumNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
        o = 1026
        self.assertEqual(s.sumNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)