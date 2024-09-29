# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Node:
    def __init__(self, key:str, index:int=1, prev:Optional['Node']=None, next:Optional['Node']=None) -> None:
        self.values = {key}
        self.index = index
        self.prev = prev
        self.next = next

    def delete(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next
        del self

    def getValue(self) -> str:
        return next(iter(self.values))
    
    def addValue(self, key:str):
        self.values.add(key)

    def removeValue(self, key:str):
        self.values.remove(key)
        # if self.isEmpty():
        #     del self
    
    def isEmpty(self) -> bool:
        return len(self.values) == 0
    
    def prevIndex(self) -> Optional[int]:
        if not self.prev:
            return None
        return self.prev.index
    
    def nextIndex(self) -> Optional[int]:
        if not self.next:
            return None
        return self.next.index

'''
Design a data structure to store the strings' count with the ability to return
the strings with minimum and maximum counts.

Note that each function must run in O(1) average time complexity.

Implement the AllOne class:
'''
class AllOne:
    '''
    Initializes the object of the data structure.
    '''
    def __init__(self):
        self.nodes:dict[int, Node] = dict()
        self.keys:dict[str, Node] = dict()
        self.max:int = 0
        self.min:int = 0

    '''
    Increments the count of the string key by 1. If key does not exist in the
    data structure, insert it with count 1.
    '''
    def inc(self, key: str) -> None:
        if key in self.keys:
            node = self.keys[key]
            index = node.index
            node.removeValue(key)
            if node.next and node.next.index == index + 1:
                node.next.addValue(key)
                self.keys[key] = node.next
            else:
                increment = Node(key, index + 1, node, node.next)
                if node.next:
                    node.next.prev = increment
                node.next = increment
                self.nodes[index + 1] = increment
                self.keys[key] = increment
            if node.isEmpty():
                if not node.prev:
                    self.min = node.next.index
                del self.nodes[index]
                node.delete()
            self.max = max(self.max, index + 1)
        elif 1 in self.nodes:
            self.nodes[1].addValue(key)
            self.keys[key] = self.nodes[1]
        else:
            node = Node(key, 1)
            if self.min > 0:
                node.next = self.nodes[self.min]
                self.nodes[self.min].prev = node
            self.nodes[1] = node
            self.keys[key] = node
            self.min = 1
            if self.max == 0:
                self.max = 1

    '''
    Decrements the count of the string key by 1. If the count of key is 0 after
    the decrement, remove it from the data structure. It is guaranteed that key
    exists in the data structure before the decrement.
    '''
    def dec(self, key: str) -> None:
        node = self.keys[key]
        index = node.index
        node.removeValue(key)
        if index - 1 in self.nodes:
            self.nodes[index - 1].addValue(key)
            self.keys[key] = self.nodes[index - 1]
        elif index - 1 == 0:
            if node.isEmpty() and node.next:
                self.min = node.next.index
            del self.keys[key]
        else:
            decrement = Node(key, index - 1, node.prev, node)
            if node.prev:
                node.prev.next = decrement
            node.prev = decrement
            self.nodes[index - 1] = decrement
            self.keys[key] = decrement
        if node.isEmpty():
            if not node.next:
                if node.prev:
                    self.max = node.prev.index
                else:
                    self.max = 0
            del self.nodes[index]
            node.delete()
        if index - 1 > 0 or self.max == 0:
            self.min = min(self.min, index - 1)

    '''
    Returns one of the keys with the maximal count. If no element exists, return
    an empty string "".
    '''
    def getMaxKey(self) -> str:
        if self.max == 0:
            return ""
        return self.nodes[self.max].getValue()

    '''
    Returns one of the keys with the minimum count. If no element exists, return
    an empty string "".
    '''
    def getMinKey(self) -> str:
        if self.min == 0:
            return ""
        return self.nodes[self.min].getValue()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = AllOne()
        s.inc("hello")
        s.inc("hello")
        self.assertEqual(s.getMaxKey(), "hello")
        self.assertEqual(s.getMinKey(), "hello")
        s.inc("leet")
        self.assertEqual(s.getMaxKey(), "hello")
        self.assertEqual(s.getMinKey(), "leet")
        s.dec("leet")
        self.assertEqual(s.getMaxKey(), "hello")
        self.assertEqual(s.getMinKey(), "hello")

    def test_two(self):
        s = AllOne()
        s.inc("hello")
        s.inc("goodbye")
        s.inc("hello")
        s.inc("hello")
        self.assertEqual(s.getMaxKey(), "hello")
        s.inc("leet")
        s.inc("code")
        s.inc("leet")
        s.dec("hello")
        s.inc("leet")
        s.inc("code")
        s.inc("code")
        self.assertEqual(s.getMaxKey(), "leet")

    def test_three(self):
        s = AllOne()
        s.inc("hello")
        s.inc("hello")
        self.assertEqual(s.getMaxKey(), "hello")
        self.assertEqual(s.getMinKey(), "hello")
        s.dec("hello")
        s.dec("hello")
        self.assertEqual(s.getMinKey(), "")
        s.inc("hello")
        self.assertEqual(s.getMinKey(), "hello")

if __name__ == '__main__':
    unittest.main(verbosity=2)