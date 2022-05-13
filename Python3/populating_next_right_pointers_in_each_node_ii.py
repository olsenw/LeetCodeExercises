# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def nextList(self):
        s = "["
        def help(node):
            if node is None:
                return
            nonlocal s
            n = node
            while n:
                s += str(n.val) + ','
                n = n.next
            else:
                s += '#,'
            help(node.left)
        help(self)
        s = s[:-1]
        return s + ']'

class Solution:
    '''
    Given a binary tree where each node has next pointer which should
    point to the next horizontal node.

    Populate each next pointer to point to its next right node. If there
    is no next right node, the next pointer should be set to NULL.

    Intially all next pointers are set to NULL.
    '''
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        s = [root]
        while s:
            n = []
            for i, j in enumerate(s):
                if j.left:
                    n.append(j.left)
                if j.right:
                    n.append(j.right)
                if i < len(s) - 1:
                    j.next = s[i + 1]
            s = n
        return root

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
        o = "[1,#,2,3,#,4,5,7,#]"
        a = s.connect(i).nextList()
        self.assertEqual(a, o)

    def test_two(self):
        s = Solution()
        self.assertEqual(s.connect(None), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)