# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

'''
Design an iterator that supports the peek operation on an existing
iterator in addition to the hasNext and the next operations
'''
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.i = iterator
        self.n = self.i.next() if self.i.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.n

    def next(self):
        """
        :rtype: int
        """
        n = self.n
        self.n = self.i.next() if self.i.hasNext() else None
        return n

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n != None

class UnitTesting(unittest.TestCase):
    # Your PeekingIterator object will be instantiated and called as such:
    # iter = PeekingIterator(Iterator(nums))
    # while iter.hasNext():
    #     val = iter.peek()   # Get the next element but not advance the iterator.
    #     iter.next()         # Should return the same value as [val].

    '''
    Due to how many parts to set up problem testing was done on Leetcode
    directly.
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)