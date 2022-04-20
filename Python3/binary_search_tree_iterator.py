# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Implement the BSTIterator class that represents an iterator over the
in-order traversal of a binary search tree (BST).

Notice that by intialiing the pointer to a non-existent smallest number,
the first call to next() will return the smallest element in the BST.

It is assumed that next() calls will always be valid. That is, there
will be at least a next number in the in-order traversal when next() is
called.
'''
# creates a list of all the values in order and iterates using the list.
class BSTIterator:
    '''
    Initializes an object of the BSTIterator class. The root of the BST
    is given as part of the constructor. The pointer should be
    initialzed to a non-existent number smaller than any element in the
    BST.
    '''
    def __init__(self, root: Optional[TreeNode]):
        self.index = 0
        self.inOrder = []
        def r(root):
            if root.left:
                r(root.left)
            self.inOrder.append(root.val)
            if root.right:
                r(root.right)
        r(root)

    '''
    Moves the pointer to the right, then returns the number at the
    pointer.
    '''
    def next(self) -> int:
        n = self.inOrder[self.index]
        self.index += 1
        return n

    '''
    Returns true if there is exists a number in the traversal to the
    right of the pointer, otherwise returns false.
    '''
    def hasNext(self) -> bool:
        return self.index < len(self.inOrder)

'''
Implement the iterator such that next() and hasNext() run in O(1) time
and use O(h) memory, where h is the height of the tree.
'''
class BSTIteratorStack:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        root = self.stack.pop()
        val = root.val
        if root.right:
            root = root.right
            while root:
                self.stack.append(root)
                root = root.left
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

'''
Could also do a Morris Traversal assuming that modifying the BST is
allowed.

Explanation for Morris Traversal:
https://en.wikipedia.org/wiki/Tree_traversal#Morris_in-order_traversal_using_threading
https://www.codingninjas.com/codestudio/library/morris-traversal-for-inorder
'''

class UnitTesting(unittest.TestCase):
    '''
    The BSTIterator object will be instantiated and called as such:
    obj = BSTIterator(root)
    param_1 = obj.next()
    param_2 = obj.hasNext()
    '''
    def test_BSTIterator(self):
        i = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        b = BSTIterator(i)
        self.assertEqual(b.next(), 3)
        self.assertEqual(b.next(), 7)
        self.assertEqual(b.hasNext(), True)
        self.assertEqual(b.next(), 9)
        self.assertEqual(b.hasNext(), True)
        self.assertEqual(b.next(), 15)
        self.assertEqual(b.hasNext(), True)
        self.assertEqual(b.next(), 20)
        self.assertEqual(b.hasNext(), False)

    def test_BSTIteratorStack(self):
        i = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        b = BSTIteratorStack(i)
        self.assertEqual(b.next(), 3)
        self.assertEqual(b.next(), 7)
        self.assertEqual(b.hasNext(), True)
        self.assertEqual(b.next(), 9)
        self.assertEqual(b.hasNext(), True)
        self.assertEqual(b.next(), 15)
        self.assertEqual(b.hasNext(), True)
        self.assertEqual(b.next(), 20)
        self.assertEqual(b.hasNext(), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)