# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
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
    Given the root of a complete binary tree, return the number of the nodes in
    the tree.

    According to Wikipedia, every level, except possibly the last, is completely
    filled in a complete binary tree, and all nodes in the last level are as far
    left as possible. It can have between 1 and 2^n nodes inclusive at the last
    level h.

    Design an algorithm that runs in less than O(n) time complexity.
    '''
    # invalid O(n) time
    def countNodes_invalid(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s = [root]
        i = 0
        while i < len(s):
            if not s[i].left:
                break
            elif not s[i].right:
                s.append(s[i].left)
                break
            else:
                s.append(s[i].left)
                s.append(s[i].right)
            i += 1
        return len(s)

    '''
    Can do dfs searches till find misalignment. 
    '''
    
    # based on leetcode discussion post by stanislav-iablokov
    # https://leetcode.com/problems/count-complete-tree-nodes/discuss/2815375/PythonC%2B%2BJavaRust-logN*logN-%2B-BONUS-complete-list-of-solutions-(explained)
    # O(log N * log N) time
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # depth of left
        curr = root
        left = 1
        while curr.left:
            left += 1
            curr = curr.left
        # depth of right
        curr = root
        right = 1
        while curr.right:
            right += 1
            curr = curr.right
        # full tree detected
        if left == right:
            return 2 ** left - 1
        # check if left and right are full trees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        o = 6
        self.assertEqual(s.countNodes(i), o)

    def test_two(self):
        s = Solution()
        i = None
        o = 0
        self.assertEqual(s.countNodes(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1)
        o = 1
        self.assertEqual(s.countNodes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)