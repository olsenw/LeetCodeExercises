# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

class Solution:
    '''
    Given two binary search trees root1 and root2, return a list 
    containing all the integers from both trees sorted in ascending
    order.
    '''
    def getAllElements_iterative_deque(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        from collections import deque
        def left(n, r):
            while n:
                r.append(n)
                n = n.left
        def right(n,r):
            if n and n.right:
                left(n.right, r)
        ans = []
        r1 = deque()
        left(root1, r1)
        r2 = deque()
        left(root2, r2)
        while r1 or r2:
            r = None
            if r1 and r2:
                r = r1 if r1[-1].val < r2[-1].val else r2
            elif r1:
                r = r1
            else:
                r = r2
            n = r.pop()
            ans.append(n.val)
            right(n, r)
            pass
        return ans

    # recursion fails if too deep (note no such case on leetcode)
    def getAllElements_recurse_then_sort(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def recurse(root, l):
            if root:
                # go left
                recurse(root.left, l)
                # middle
                l.append(root.val)
                # go right
                recurse(root.right, l)
            else:
                return
        s = []
        recurse(root1, s)
        recurse(root2, s)
        return sorted(s)

    # recursion fails if too deep (note no such case on leetcode)
    def getAllElements_recurse_then_merge(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def recurse(root, l):
            if root:
                # go left
                recurse(root.left, l)
                # middle
                l.append(root.val)
                # go right
                recurse(root.right, l)
            else:
                return
        r1 = []
        recurse(root1, r1)
        r2 = []
        recurse(root2, r2)
        s = []
        i = 0
        j = 0
        while i < len(r1) and j < len(r2):
            if r1[i] < r2[j]:
                s.append(r1[i])
                i += 1
            else:
                s.append(r2[j])
                j += 1
        for n in r1[i:]:
            s.append(n)
        for n in r2[j:]:
            s.append(n)
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(2, TreeNode(1), TreeNode(4))
        r = TreeNode(1, TreeNode(0), TreeNode(3))
        o = [0,1,1,2,3,4]
        self.assertEqual(s.getAllElements_recurse_then_sort(i,r), o)
        self.assertEqual(s.getAllElements_recurse_then_merge(i,r), o)
        self.assertEqual(s.getAllElements_iterative_deque(i,r), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, None, TreeNode(8))
        r = TreeNode(8, TreeNode(1))
        o = [1,1,8,8]
        self.assertEqual(s.getAllElements_recurse_then_sort(i,r), o)
        self.assertEqual(s.getAllElements_recurse_then_merge(i,r), o)
        self.assertEqual(s.getAllElements_iterative_deque(i,r), o)

    def test_three(self):
        import sys
        s = Solution()
        i = None
        for j in range(0,5000):
            n = TreeNode(j, i)
            i = n
        r = None
        for j in range(5000,10000):
            n = TreeNode(j, r)
            r = n
        o = [i for i in range(10000)]
        # self.assertEqual(s.getAllElements_recurse_then_sort(i,r), o)
        # self.assertEqual(s.getAllElements_recurse_then_merge(i,r), o)
        self.assertEqual(s.getAllElements_iterative_deque(i,r), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)