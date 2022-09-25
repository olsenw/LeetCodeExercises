# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Design an implementation of the circular queue. The circular queue is a
linear data structure in which the operations are performed based on FIFO 
(First In First Out) principle and the last position is connected back to
the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that it can make use of spaces
in front of the queue. In a normal queue, once the queue becomes full, it
cannot insert the next element even if there is a space in front of the
queue. But using the circular queue, it is possible to use the space to
store new values.

Implement the queue without using a built-in queue data structure.
'''
class MyCircularQueue:
    '''
    Initializes the object with the size of the queue to be k.
    '''
    def __init__(self, k: int):
        self.queue = [None] * k
        self.index = 0
        self.elements = 0

    '''
    Inserts an element into the circular queue. Return true if the operation is
    successful.
    '''
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.queue[((self.index + self.elements) % len(self.queue))] = value
        self.elements += 1
        return True

    '''
    Deletes an element from the circular queue. Return true if the operation is
    successful.
    '''
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.index = (self.index + 1) % len(self.queue)
        self.elements -= 1
        return True

    '''
    Gets the front item from the queue. If the queue is empty return -1.
    '''
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.index]

    '''
    Gets the last item from the queue. If the queue is empty return -1.
    '''
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[(self.index + self.elements - 1) % len(self.queue)]

    '''
    Checks whether the circular queue is empty or not.
    '''
    def isEmpty(self) -> bool:
        return self.elements == 0

    '''
    Checks whether the circular queue is full or not.
    '''
    def isFull(self) -> bool:
        return self.elements == len(self.queue)

class UnitTesting(unittest.TestCase):
    def test(self):
        q = MyCircularQueue(3)
        self.assertTrue(q.enQueue(1))
        self.assertTrue(q.enQueue(2))
        self.assertTrue(q.enQueue(3))
        self.assertFalse(q.enQueue(4))
        self.assertEqual(q.Rear(), 3)
        self.assertEqual(q.Front(), 1)
        self.assertTrue(q.isFull())
        self.assertTrue(q.deQueue())
        self.assertTrue(q.enQueue(4))
        self.assertEqual(q.Rear(), 4)
        self.assertEqual(q.Front(), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)