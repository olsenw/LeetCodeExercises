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

class Solution:
    '''
    Given the root of a binary tree where each node has a value in the range [0
    , 25] representing the letters 'a' to 'z'.

    Return the lexicographically smallest string that starts at a leaf of this
    tree and ends at the root.

    As a reminder, any shorter prefix of a string is lexicographically smaller.

    A leaf of a node is a node that has no children.
    '''
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        answer = 'z' * 8500
        stack = []
        def dfs(node: TreeNode):
            nonlocal answer
            stack.append(chr(97 + node.val))
            if node.left is None and node.right is None:
                s = ''.join(stack[::-1])
                if s < answer:
                    answer = s
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()
        dfs(root)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(0), TreeNode(2)))
        o = "adz"
        self.assertEqual(s.smallestFromLeaf(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(2, TreeNode(2, None, TreeNode(1, TreeNode(0))), TreeNode(1, TreeNode(0)))
        o = "abc"
        self.assertEqual(s.smallestFromLeaf(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)