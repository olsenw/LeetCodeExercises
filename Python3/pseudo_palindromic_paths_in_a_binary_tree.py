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
    Given a binary tree where node values are digits from 1 to 9. A path
    in the binary tree is said to be pseudo-palindromic if at least one
    permutation of the nodes values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from the root
    node to leaf nodes.
    '''
    def pseudoPalindromicPaths_pass_slow(self, root: Optional[TreeNode]) -> int:
        count = [0] * 10
        answer = 0
        def dfs(node):
            nonlocal answer
            nonlocal count
            count[node.val] += 1
            if node.left is None and node.right is None:
                if sum(c % 2 for c in count) <= 1:
                    answer += 1
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            count[node.val] -= 1
        dfs(root)
        return answer

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        answer = 0
        count = [False]*10
        def dfs(node):
            nonlocal answer
            nonlocal count
            count[node.val] = not count[node.val]
            if not node.left and not node.right:
                if sum(count) <= 1:
                    answer += 1
            else:
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)
            count[node.val] = not count[node.val]
        dfs(root)
        return answer

    '''
    From Leetcode solution
    https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solution/
    
    Could do this using bit masking instead of array

    # check if single bit is one
    path & (path - 1) == 0

    # update parity count
    path = path ^ (1 << node.val)
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
        o = 2
        self.assertEqual(s.pseudoPalindromicPaths(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))), TreeNode(1))
        o = 1
        self.assertEqual(s.pseudoPalindromicPaths(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = 1
        self.assertEqual(s.pseudoPalindromicPaths(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)