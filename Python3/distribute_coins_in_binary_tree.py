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
    Given the root of a binary tree with n nodes where each node in the tree has
    node.val coins. There are n coins in total throughout the whole tree.

    In one move, it is possible to choose two adjacent nodes and move one coin
    from one node to another. A move may be from parent to child, or from child
    to parent.

    Return the minimum number of moves required to make every node have exactly
    one coin.
    '''
    # based on Leetcode Editorial
    # https://leetcode.com/problems/distribute-coins-in-binary-tree/editorial/?envType=daily-question&envId=2024-05-18
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node: Optional[TreeNode]):
            nonlocal answer
            # 
            if node is None:
                return 0
            # get number of coins that can be transferred from left subtree
            # negative number represents coins needed, positive number is excess coins to transfer
            l = dfs(node.left)
            # get number of coins that can be transferred from right subtree
            r = dfs(node.right)
            # number of moves to move coins
            answer += node.val - 1 + abs(l) + abs(r)
            # how many coins can be transferred
            return node.val - 1 + l + r
        dfs(root)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(0), TreeNode(0))
        o = 2
        self.assertEqual(s.distributeCoins(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(0, TreeNode(3), TreeNode(0))
        o = 3
        self.assertEqual(s.distributeCoins(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(3, TreeNode(0, TreeNode(2)), TreeNode(0,TreeNode(0)))
        o = 4
        self.assertEqual(s.distributeCoins(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)