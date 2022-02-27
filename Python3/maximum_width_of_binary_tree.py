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
    Given the root of a binary tree, return the maximum width of the 
    given tree.

    The maximum width of a tree is the maximum width among all levels.

    The width of one level is defined as the length between the
    end-nodes (the leftmost and rightmost non-null nodes), where the
    null nodes between the end-nodes are also counted into the length
    calculation.
    '''
    # time limit exceeded (94/113 test cases)
    def widthOfBinaryTree_slow(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        best = 0
        while queue:
            best = max(best, len(queue))
            nq = []
            for q in queue:
                if q:
                    nq.append(q.left)
                    nq.append(q.right)
                else:
                    nq += [None, None]
            i = 0
            while i < len(nq) and nq[i] == None:
                i += 1
            j = len(nq) - 1
            while nq[j] == None and j > i:
                j -= 1
            queue = nq[i:j+1]
        return best

    # same idea as above but does not pad out queue with Nones
    # work smarter not harder
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        0
        0   1
        0 1 2 3
        01234567
        (n * 2) left
        (n * 2 + 1) right
        '''
        queue = [(0, root)]
        best = 0
        while queue:
            best = max(best, queue[-1][0] - queue[0][0] + 1)
            nq = []
            for v, n in queue:
                if n.left:
                    nq.append((v * 2, n.left))
                if n.right:
                    nq.append((v * 2 + 1, n.right))
            queue = nq
        return best

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(
                1,
                TreeNode(
                        3,
                        TreeNode(5),
                        TreeNode(3)
                ),
                TreeNode(
                    2,
                    None,
                    TreeNode(9)
                )
            )
        o = 4
        self.assertEqual(s.widthOfBinaryTree(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(
                1,
                TreeNode(
                        3,
                        TreeNode(5),
                        TreeNode(3)
                ),
                None
            )
        o = 2
        self.assertEqual(s.widthOfBinaryTree(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(
                1,
                TreeNode(
                        3,
                        TreeNode(5),
                        None
                ),
                TreeNode(2)
            )
        o = 2
        self.assertEqual(s.widthOfBinaryTree(i), o)

    def test_four(self):
        s = Solution()
        i = TreeNode(1)
        o = 1
        self.assertEqual(s.widthOfBinaryTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)