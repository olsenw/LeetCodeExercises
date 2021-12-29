# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional
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
    Given a perfect binary tree where all leaves are on the same level
    and every parent has two children. The binary tree nodes have 
    following definition:
        Node
            int val
            Node left
            Node right
            Node next
    Intially all next pointers are set to NULL.

    Populate the next pointers such that it points to the next right
    node. If there is no next right node, the next pointer should be set
    to NULL. (ie next pointer connects nodes on the same level of in tree)
    '''
    # O(n) time O(2^d) space
    def connect_bfs(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root
        from collections import deque
        d = deque()
        d.append(root)
        d.append(None)
        while d:
            n = d.popleft()
            if n is None and len(d) > 1:
                d.append(None)
                continue
            elif n is None:
                continue
            else:
                n.next = d[0]
                if n.left:
                    d.append(n.left)
                    d.append(n.right)
        return root

    # O(n) time O(1) space solution based on leetcode discussions
    def connect_dfs(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root
        if root.left:
            l = root.left
            r = root.right
            # recurse
            self.connect_dfs(l)
            self.connect_dfs(r)
            # connect
            while l:
                l.next = r
                l = l.right
                r = r.left
        return root

    '''
    copied from leetcode discuss and saved for own reference
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/1653910/easy-to-understand-two-pointer-approach
    
    starts at root and goes down left of tree
    connects all the nodes one level down
    follows node accesses similar to dfs approach
    '''
    def connect_twopointer(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        verticalPtr = root

        while verticalPtr is not None:
            horizontalPtr = verticalPtr
            while horizontalPtr is not None:
                if horizontalPtr.left is not None:
                    horizontalPtr.left.next = horizontalPtr.right
                if horizontalPtr.right is not None and horizontalPtr.next is not None:
                    horizontalPtr.right.next = horizontalPtr.next.left
                horizontalPtr = horizontalPtr.next
            verticalPtr = verticalPtr.left
        return root

class UnitTesting(unittest.TestCase):
    def test_one_bfs(self):
        s = Solution()
        i = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        o = "[1,#,2,3,#,4,5,6,7,#]"
        a = s.connect_bfs(i).nextList()
        self.assertEqual(a, o)

    def test_two_bfs(self):
        s = Solution()
        i = None
        o = None
        a = s.connect_bfs(i)
        self.assertEqual(a, o)

    def test_one_dfs(self):
        s = Solution()
        i = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        o = "[1,#,2,3,#,4,5,6,7,#]"
        a = s.connect_dfs(i).nextList()
        self.assertEqual(a, o)

    def test_two_dfs(self):
        s = Solution()
        i = None
        o = None
        a = s.connect_dfs(i)
        self.assertEqual(a, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)