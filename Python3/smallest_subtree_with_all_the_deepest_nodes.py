# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict, deque
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
    def __eq__(self, value:"TreeNode"):
        return self.val == value.val and self.left == value.left and self.right == value.right

class Solution:
    '''
    Given the root of a binary tree, the depth of each node is the shortest
    distance to the root.

    Return the smallest subtree such that it contains all the deepest nodes in
    the original tree.

    A node is called the deepest if it has the largest depth possible among any
    node in the entire tree.

    The subtree of a node is a tree consisting of that node, plus the set of all
    descendants of that node.
    '''
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = defaultdict(list)
        m = 0
        def dfs(node:Optional[TreeNode], depth:int):
            nonlocal m
            if node is None:
                return
            d[depth].append(node)
            m = max(m, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            return 
        dfs(root,0)
        c = len(d[m])
        answer = root
        high = 0
        def find(node:Optional[TreeNode], depth:int) -> int:
            nonlocal answer
            nonlocal high
            if node is None:
                return 0
            if depth == m:
                if 1 == c and depth > high:
                    high = depth
                    answer = node
                return 1
            a = find(node.left, depth+1) + find(node.right, depth+1)
            if a == c and depth > high:
                high = depth
                answer = node
            return a
        find(root,0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        o = TreeNode(2, TreeNode(7), TreeNode(4))
        self.assertEqual(s.subtreeWithAllDeepest(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        o = TreeNode(1)
        self.assertEqual(s.subtreeWithAllDeepest(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(0, TreeNode(1, None, TreeNode(2)), TreeNode(3))
        o = TreeNode(2)
        self.assertEqual(s.subtreeWithAllDeepest(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)