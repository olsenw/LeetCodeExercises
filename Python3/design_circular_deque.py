# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Deque, List, Dict, Set, Optional

'''
Design an implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:
'''
class MyCircularDeque_cheating:
    '''
    Initializes the deque with a maximum size of k.
    '''
    def __init__(self, k: int):
        self.deque = Deque()
        self.length = k

    '''
    Adds an item at the front of the Deque. Returns true if the operation is
    successful, or false otherwise.
    '''
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.appendleft(value)
        return True

    '''
    Adds an item at the rear of Deque. Return true if the operation is
    successful, or false otherwise.
    '''
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    '''
    Deletes an item from the front of the Deque. Returns true if the operation
    is successful, or false otherwise.
    '''
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    '''
    Deletes an item from the rear of Deque. Returns true if the operation is
    successful, or false otherwise.
    '''
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True

    '''
    Returns the front item from the Deque Returns -1 if the deque is empty.
    '''
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    '''
    Returns the last item from Deque. Returns -1 if the deque is empty.
    '''
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    '''
    Returns true if the deque is empty, or false otherwise.
    '''
    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    '''
    Returns true if the deque is full, or false otherwise
    '''
    def isFull(self) -> bool:
        return len(self.deque) == self.length

class MyCircularDeque:
    def __init__(self, k: int):
        self.l = [0] * k
        self.front = 0
        self.last = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.l[self.front % len(self.l)] = value
        # self.front = (self.front - 1) % len(self.l)
        self.front -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # self.last = (self.last + 1) % len(self.l)
        self.last += 1
        self.l[self.last % len(self.l)] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        # self.front = (self.front + 1) % len(self.l)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.last -= 1
        # self.last = (self.last - 1) % len(self.l)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[(self.front + 1) % len(self.l)]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.last % len(self.l)]

    def isEmpty(self) -> bool:
        return self.front == self.last

    def isFull(self) -> bool:
        return self.last - self.front == len(self.l)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = MyCircularDeque(3)
        self.assertEqual(s.insertLast(1), True)
        self.assertEqual(s.insertLast(2), True)
        self.assertEqual(s.insertFront(3), True)
        self.assertEqual(s.insertFront(4), False)
        self.assertEqual(s.getRear(), 2)
        self.assertEqual(s.isFull(), True)
        self.assertEqual(s.deleteLast(), True)
        self.assertEqual(s.insertFront(4), True)
        self.assertEqual(s.getFront(), 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)