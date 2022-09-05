# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    '''
    Given an n-ary tree, return the level order traversal of its nodes'
    values.
    '''
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        def dfs(node, depth):
            nonlocal levels
            if not node:
                return
            if depth < len(levels):
                levels[depth].append(node.val)
            else:
                levels.append([node.val])
            if node.children:
                for n in node.children:
                    dfs(n, depth + 1)
        dfs(root, 0)
        return levels

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        o = [[1],[3,2,4],[5,6]]
        self.assertEqual(s.levelOrder(i), o)

    def test_two(self):
        s = Solution()
        i = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
        o = [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
        self.assertEqual(s.levelOrder(i), o)

    def test_three(self):
        s = Solution()
        i = None
        o = []
        self.assertEqual(s.levelOrder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)