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
    Given the root node of a binary search tree (BST) and a value to
    insert into the tree. Return the root node of the BST after the
    insertion.

    It is guaranteed that the new value does not exist in the original
    BST.

    There may be multiple valid ways to perform the insertion. As long
    as the resulting tree is a BST it will be accepted.
    (Not the case in my unit tests. They accept only one answer.)
    '''
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        n, prev = root, None
        while n:
            prev = n
            # not >= because constraint of all values being unique
            if n.val > val:
                n = n.left
            else:
                n = n.right
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        return root

    # based on discussion post on leetcode
    # https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/1683883/Python3-ITERATIVE-(-)-Explained
    # two differences to above solution
    #   variable assignment in the while loop
    #   using less than instead of greater than
    # not sure why this one takes half the time...
    def insertIntoBST_faster(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        n, c = root, None
        while n:
            c = n
            # not >= because constraint of all values being unique
            if val < c.val:
                n = c.left
            else:
                n = c.right
        if val < c.val:
            c.left = TreeNode(val)
        else:
            c.right = TreeNode(val)
        return root

class UnitTesting(unittest.TestCase):
    def __compare(self, answer, root):
        from collections import deque
        d = deque()
        sa, sr = set(), set()
        d.append((answer, root))
        while d:
            l, r = d.pop()
            if not l and not r:
                print(type(l), type(r))
                continue
            print(l.val,r.val)
            self.assertEqual(l.val, r.val)
            d.append((l.left, r.left))
            d.append((l.right, r.right))
            sa.add(l.val)
            sr.add(r.val)
        self.assertEqual(sa, sr)

    def test_one(self):
        s = Solution()
        i = TreeNode(4, 
          TreeNode(2, 
            TreeNode(1), 
            TreeNode(3)
          ), 
          TreeNode(7)
        )
        v = 5
        o = TreeNode(4, 
          TreeNode(2, 
            TreeNode(1), 
            TreeNode(3)
          ), 
          TreeNode(7, 
            TreeNode(5)
          )
        )
        # self.__compare(s.insertIntoBST(i, v), o)
        self.__compare(s.insertIntoBST_faster(i, v), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(40, 
          TreeNode(20, 
            TreeNode(10), 
            TreeNode(30)
          ), 
          TreeNode(60, 
            TreeNode(50), 
            TreeNode(70)
          ), 
        )
        v = 25
        o = TreeNode(40, 
          TreeNode(20, 
            TreeNode(10), 
            TreeNode(30,
              TreeNode(25)
            )
          ), 
          TreeNode(60, 
            TreeNode(50), 
            TreeNode(70)
          ), 
        )
        # self.__compare(s.insertIntoBST(i, v), o)
        self.__compare(s.insertIntoBST_faster(i, v), o)

    def test_three(self):
        s = Solution()
        i = None
        v = 5
        o = TreeNode(5)
        # self.__compare(s.insertIntoBST(i, v), o)
        self.__compare(s.insertIntoBST_faster(i, v), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    # '''
    # tests to see if < is faster than >
    # '''
    # import time
    # import random
    # from statistics import mean
    # def timingless():
    #     c = 0
    #     t1 = time.time_ns()
    #     for i in range(1000000):
    #         if i - c < i + c:
    #             c += 1
    #     t2 = time.time_ns()
    #     return t2-t1
    # def timinggreat():
    #     c = 0
    #     t1 = time.time_ns()
    #     for i in range(1000000):
    #         if i + c > i - c:
    #             c += 1
    #     t2 = time.time_ns()
    #     return t2-t1
    # l = []
    # g = []
    # for i in range(10000):
    #     if random.choice([True, False]):
    #         l.append(timingless())
    #         g.append(timinggreat())
    #     else:
    #         g.append(timinggreat())
    #         l.append(timingless())
    # print("l", mean(l))
    # print("g", mean(g))