# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
This two linked list took forever
'''
class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.parent = None
        self.child = None
    def insert(self, parent):
        self.parent = parent
        if parent.child:
            parent.child.parent = self
        self.child = parent.child
        parent.child = self
    def remove(self):
        self.parent.child = self.child
        self.child.parent = self.parent
        self.parent = None
        self.child = None
    def toList(self):
        a = []
        curr = self
        while curr is not None:
            a.append(curr.val)
            curr = curr.child
        return a
    def backward(self):
        a = []
        curr = self
        while curr is not None:
            a.append(curr.val)
            curr = curr.parent
        return a

'''
Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class such that get and put run in O(1) average time
complexity.
'''
class LRUCache:
    '''
    Initialize the LRU cache with positive size capacity.
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = dict()
        self.head = Node(-1,-1)
        self.tail = self.head
    '''
    Return the value of the key if the key exists, otherwise return -1.
    '''
    def get(self, key: int) -> int:
        if key in self.lru:
            if self.lru[key] is not self.tail:
                self.lru[key].remove()
                self.lru[key].insert(self.tail)
                self.tail = self.lru[key]
            return self.tail.val
        else:
            return -1
    '''
    Update the value of the key if the key exists. Otherwise, add the key-value
    pair to the cahce. If the number of keys exceeds the capacity from this
    operation, evict the least recently used key.
    '''
    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            if self.lru[key] is self.tail:
                self.tail.val = value
            else:
                self.lru[key].remove()
                self.lru[key].insert(self.tail)
                self.tail = self.lru[key]
                self.tail.val = value
        else:
            self.lru[key] = Node(key, value)
            self.lru[key].insert(self.tail)
            self.tail = self.lru[key]
            if len(self.lru) > self.capacity:
                if self.head.child is self.tail:
                    self.tail = self.head
                del self.lru[self.head.child.key]
                self.head.child.remove()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        l = LRUCache(2)
        l.put(1,1)
        l.put(2,2)
        self.assertEqual(l.get(1), 1)
        l.put(3,3)
        self.assertEqual(l.get(2), -1)
        l.put(4,4)
        self.assertEqual(l.get(1), -1)
        self.assertEqual(l.get(3), 3)
        self.assertEqual(l.get(4), 4)

    def test_two(self):
        l = LRUCache(2)
        l.put(2,1)
        l.put(1,1)
        l.put(2,3)
        l.put(4,1)
        self.assertEqual(l.get(1), -1)
        self.assertEqual(l.get(2), 3)

    def test_three(self):
        l = LRUCache(1)
        l.put(1,1)
        self.assertEqual(l.get(1), 1)
        l.put(2,2)
        self.assertEqual(l.get(1), -1)
        self.assertEqual(l.get(2), 2)
        l.put(3,3)
        self.assertEqual(l.get(1), -1)
        self.assertEqual(l.get(2), -1)
        self.assertEqual(l.get(3), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)