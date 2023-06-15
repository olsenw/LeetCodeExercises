# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
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
    Given the root of a binary tree, the level of its root is 1, the level of
    its children is 2, and so on.

    Return the smallest level x such that the sum of all the values of nodes at
    level x is maximal.
    '''
    def maxLevelSum_dfs_counter(self, root: Optional[TreeNode]) -> int:
        c = Counter()
        def dfs(node, level):
            if not node:
                return
            c[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return max(((c[i], i) for i in c), key=lambda x:(x[0], -x[1]))[1]

    def maxLevelSum_dfs_list(self, root: Optional[TreeNode]) -> int:
        a = [-10**6]
        def dfs(node, level):
            if not node:
                return
            if level == len(a):
                a.append(node.val)
            else:
                a[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return max(enumerate(a), key=lambda x: (x[1],-x[0]))[0]

    def maxLevelSum_bfs(self, root: Optional[TreeNode]) -> int:
        best = -10**6
        level = 0
        l = 1
        q = [root]
        while q:
            n = []
            s = 0
            for i in q:
                s += i.val
                if i.left:
                    n.append(i.left)
                if i.right:
                    n.append(i.right)
            if best < s:
                best = s
                level = l
            q = n
            l += 1
        return level

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
        o = 2
        self.assertEqual(s.maxLevelSum_bfs(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(-100,TreeNode(-200,TreeNode(-20),TreeNode(-5)),TreeNode(-300,TreeNode(-10)))
        o = 3
        self.assertEqual(s.maxLevelSum_bfs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)