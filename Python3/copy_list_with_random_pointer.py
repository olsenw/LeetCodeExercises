# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    '''
    A linked list of length n is given such that each node contains an
    additional random pointer, which could point to any node in the
    list, or null.

    Construct a deep copy of the list. The deep copy should consist of
    exactly n brand new nodes, where each new node has its value set to
    the value of its corresponding original node. Both the next and 
    random pointer of the new nodes should point to new nodes in the
    copied list such that the original list and copied list represent
    the same list state. None of the pointers in the new list should
    point to nodes in the original list.

    Return the head of the copied linked list.
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        rand = dict()
        curr = dummy
        orig = head
        # allocate new nodes
        while orig:
            # create new node
            curr.next = Node(orig.val)
            # add to hashmap
            rand[id(orig)] = curr.next
            # advance pointers
            curr = curr.next
            orig = orig.next
        # copy random pointers
        orig = head
        while orig:
            if id(orig.random) in rand:
                rand[id(orig)].random = rand[id(orig.random)]
            # advance pointers
            orig = orig.next
        return dummy.next

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        l = [Node(7), Node(13), Node(11), Node(10), Node(1)]
        l[1].random = l[0]
        l[2].random = l[4]
        l[3].random = l[2]
        l[4].random = l[0]
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        o = s.copyRandomList(l[0])
        # inspect using debugger... too lazy to write equality check
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)