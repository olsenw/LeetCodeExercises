# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
There is a stream of n (idKey, value) pairs arriving in an arbitrary order,
where idKey is an integer between 1 and n and value is a string. No two
pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by
returning a chunk (list) of values after each insertion. The concatenation
of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:
* OrderedStream(int n) Constructs the stream to take n values.
* String[] insert(int idKey, String value) Inserts the pair (idKey, value)
  into the stream, then returns the largest possible chunk of currently
  inserted values that appear next in the order.
'''
class OrderedStream:

    def __init__(self, n: int):
        self.chunks = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunks[idKey-1] = value
        chunk = []
        while self.ptr < len(self.chunks) and self.chunks[self.ptr] is not None:
            chunk.append(self.chunks[self.ptr])
            self.ptr += 1
        return chunk

class UnitTesting(unittest.TestCase):
    # tested on leetcode
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)