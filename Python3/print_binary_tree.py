# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
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
    Given the root of a binary tree, construct a 0-indexed m x n string matrix
    res that represents a formatted layout of the tree. The formatted layout
    matrix should be constructed using the following rules:
    * The height of the tree is height and the number of rows m should be equal
      to height + 1.
    * The number of columns n should equal 2^(height+1) - 1.
    * Place the root node in the middle of the top row (more formally, at
      location res[0][(n-1)/2]).
    * For each node that has been placed in the matrix at position res[r][c],
      place its left child at res[r+1][c-2^(height + 1)] and its right child at
      res[r+1][c+2^(height + 1)].
    * Continue this process until all the nodes in the tree have been placed.
    * Any empty cells should contain the empty string "".

    Return the constructed matrix res.
    '''
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def depth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        m = depth(root)
        n = 2 ** m - 1
        answer = [[""] * n for _ in range(m)]
        q = deque([(0,(n-1)//2,root)])
        while q:
            r,c,t = q.popleft()
            answer[r][c] = str(t.val)
            if t.left is not None:
                q.append((r+1,c - 2**(m - r - 2), t.left))
            if t.right is not None:
                q.append((r+1,c + 2**(m - r - 2), t.right))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2))
        o = [["","1",""],
             ["2","",""]]
        self.assertEqual(s.printTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        o = [["","","","1","","",""],
             ["","2","","","","3",""],
             ["","","4","","","",""]]
        self.assertEqual(s.printTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)