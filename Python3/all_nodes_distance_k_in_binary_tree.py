# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree, the value of a target node target, and an
    integer k, return an array of the values of all nodes that have a distance k
    from the target node.
    '''
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        answer = []
        q = deque([(target,0)])
        v = set()
        while q:
            n,d = q.popleft()
            if n is None or n.val in v or d > k:
                continue
            v.add(n.val)
            if d == k:
                answer.append(n.val)
            q.append((n.left,d+1))
            q.append((n.right,d+1))
            q.append((n.parent,d+1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3,
                    TreeNode(5, 
                            TreeNode(6), 
                            TreeNode(2, 
                                    TreeNode(7),
                                    TreeNode(4)
                                    )
                            ),
                    TreeNode(1, TreeNode(0), TreeNode(8))
                    )
        j = i.left
        k = 2
        o = [7,4,1]
        self.assertEqual(s.distanceK(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1)
        j = i
        k = 3
        o = []
        self.assertEqual(s.distanceK(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)