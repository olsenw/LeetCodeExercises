# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    '''
    Given a double linked list, which contains nodes that have a next pointer, a
    previous pointer, and an additional child pointer. This child pointer may or
    may not point to a separate doubly linked list, also containing these
    special nodes. These child lists may have one or more children of their own,
    and so on, to produce a multilevel data structure.

    Given the head of the first level of the list, flatten the list so that all
    the nodes appear in a single-level, doubly linked list. Let curr be a node
    with a child list. The nodes in the child list should appear after curr and
    before curr.next in the flattened list.

    Return the head of the flattened list. The nodes in the list must have all
    of their child pointers set to null.
    '''
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def f(node: Optional[Node]) -> List[Node]:
            a = []
            c = node
            while c:
                a.append(c.val)
                if c.child:
                    a.extend(f(c.child))
                c = c.next
            return a
        a = [Node(n, None, None, None) for n in f(head)]
        for i in range(len(a) - 1):
            a[i].next = a[i+1]
        for i in range(len(a) - 1, 0, -1):
            a[i].prev = a[i-1]
        return a[0] if len(a) else None

'''
Feel like I should be able to do this inplace
'''

class UnitTesting(unittest.TestCase):
    '''
    Tested online
    Below test is invalid used for debugging
    '''
    def test_one(self):
        s = Solution()
        n = [Node(0),Node(1),Node(2),Node(3),Node(4),Node(5),Node(6),Node(7),Node(8),Node(9),Node(10),Node(11)]
        # next
        n[0].next = n[1]
        n[1].next = n[2]
        n[2].next = n[3]
        n[3].next = n[4]
        n[4].next = n[5]
        n[6].next = n[7]
        n[7].next = n[8]
        n[8].next = n[9]
        n[10].next = n[11]
        # prev
        n[1].prev = n[0]
        n[2].prev = n[1]
        n[3].prev = n[2]
        n[4].prev = n[3]
        n[5].prev = n[4]
        n[7].prev = n[6]
        n[8].prev = n[7]
        n[9].prev = n[8]
        n[11].prev = n[10]
        # child
        n[2].child = n[6]
        n[7].child = n[10]
        self.assertEqual(s.flatten(n[0]), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)