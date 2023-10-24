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
    Given the root of a binary tree, return an array of the largest value in
    each row of the tre(0-indexed).
    '''
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def dfs(node, depth):
            if not node:
                return
            elif depth == len(answer):
                answer.append(node.val)
            else:
                answer[depth] = max(answer[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2), TreeNode(3))
        o = [1,3]
        self.assertEqual(s.largestValues(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
        o = [1,3,9]
        self.assertEqual(s.largestValues(i), o)

    def test_three(self):
        s = Solution()
        i = None
        o = []
        self.assertEqual(s.largestValues(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)