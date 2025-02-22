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
    def __eq__(self, value):
        return self.val == value.val and self.left == value.left and self.right == value.right

class Solution:
    '''
    A preorder depth-first search (DFS) on the root of a binary tree.

    At each node in this traversal, D dashes are outputted (where D is the depth
    of this node), then the value of the node is outputted. If the depth of a
    node is D, the depth of its immediate child is D + 1. The depth of the root
    node is 0.

    If a node has only one child, that child is guaranteed to be the left child.

    Given the output traversal of this traversal, recover the tree and return
    its root.
    '''
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        depth = 0
        value = ""
        change = False
        for c in traversal:
            if c == '-':
                if change:
                    change = False
                    nodes.append((depth,int(value)))
                    depth = 0
                    value = ""
                depth += 1
            else:
                change = True
                value += c
        nodes.append((depth,int(value)))
        index = 0
        def dfs(depth:int)->TreeNode:
            nonlocal index
            if index == len(nodes) or nodes[index][0] < depth:
                return None
            answer = TreeNode(nodes[index][1])
            index += 1
            answer.left = dfs(depth+1)
            answer.right = dfs(depth+1)
            return answer
        return dfs(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1-2--3--4-5--6--7"
        o = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
        self.assertEqual(s.recoverFromPreorder(i), o)

    def test_two(self):
        s = Solution()
        i = "1-2--3---4-5--6---7"
        o = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5, TreeNode(6, TreeNode(7))))
        self.assertEqual(s.recoverFromPreorder(i), o)

    def test_three(self):
        s = Solution()
        i = "1-401--349---90--88"
        o = TreeNode(1, TreeNode(401, TreeNode(349, TreeNode(90)), TreeNode(88)))
        self.assertEqual(s.recoverFromPreorder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)