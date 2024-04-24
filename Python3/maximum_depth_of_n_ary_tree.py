# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    '''
    Given a n-ary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.
    '''
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        answer = 1
        for c in root.children:
            answer = max(answer, 1 + self.maxDepth(c))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i =Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        o = 3
        self.assertEqual(s.maxDepth(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)