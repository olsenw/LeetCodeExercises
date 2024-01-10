# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
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
    Given the root of a binary tree with unique value, and an integer start. At
    minute 0, an infection starts from the node with value start.

    Each minute, a node becomes infected if:
    * The node is currently uninfected.
    * The node is adjacent to an infected node.

    Return the number of minutes needed for the entire tree to be infected.
    '''
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        target = None
        def dfs(node: Optional[TreeNode]):
            nonlocal target
            if not node:
                return
            if node.val == start:
                target = node
            if node.left:
                graph[node.val].append(node.left)
                graph[node.left.val].append(node)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right)
                graph[node.right.val].append(node)
                dfs(node.right)
        dfs(root)
        answer = 0
        infected = set()
        q = deque([(target,0)])
        while q:
            n,t = q.popleft()
            infected.add(n.val)
            answer = max(answer, t)
            for i in graph[n.val]:
                if i.val not in infected:
                    q.append((i, t+1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10), TreeNode(6)))
        j = 3
        o = 4
        self.assertEqual(s.amountOfTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        j = 1
        o = 0
        self.assertEqual(s.amountOfTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)