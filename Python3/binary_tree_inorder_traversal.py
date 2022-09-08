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
    Given the root of a binary tree, return the inorder traversal of its
    nodes' values.
    '''
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def inorder(node, answer):
            if node is None:
                return
            inorder(node.left, answer)
            answer.append(node.val)
            inorder(node.right, answer)
        inorder(root, answer)
        return answer

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        s = []
        curr = root
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            a.append(curr.val)
            curr = curr.right
        return a

    '''
    could reorganize the tree such that if becomes linear in desired
    order (Morris traversal / threaded binary tree)
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        o = [1,3,2]
        self.assertEqual(s.inorderTraversal(i), o)

    def test_two(self):
        s = Solution()
        i = None
        o = []
        self.assertEqual(s.inorderTraversal(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = [1]
        self.assertEqual(s.inorderTraversal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)