# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class SortedDict:
    def __init__(self):
        self.l = [0]
        self.d = {0:0}

    def get(self, index):
        n = len(self.l)
        i = bisect.bisect_left(self.l, index)
        if i < n and self.l[i] == index:
            return self.d[index]
        else:
            return self.d[self.l[i - 1]]

    def set(self, index, value):
        if self.l[-1] != index:
            self.l.append(index)
        self.d[index] = value

'''
Implement a SnapshotArray that supports the following interface:
'''
class SnapshotArray:
    '''
    Initializes an array-like data structure with the given length. Initially,
    each element equals 0.
    '''
    def __init__(self, length: int):
        self.s = 0
        self.d = [SortedDict() for _ in range(length)]

    '''
    Sets the element at the given index to be equal to val.
    '''
    def set(self, index: int, val: int) -> None:
        self.d[index].set(self.s, val)

    '''
    Takes a snapshot of the array and returns the snap_id: the total number of
    times snap has been called minus 1.
    '''
    def snap(self) -> int:
        self.s += 1
        return self.s - 1

    '''
    Returns the value at the given index, at the time of the given the snapshot
    id.
    '''
    def get(self, index: int, snap_id: int) -> int:
        return self.d[index].get(snap_id)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = SnapshotArray(3)
        s.set(0,5)
        self.assertEqual(s.snap(), 0)
        s.set(0,6)
        self.assertEqual(s.get(0,0), 5)
        self.assertEqual(s.get(0,1), 6)
        self.assertEqual(s.snap(), 1)
        self.assertEqual(s.snap(), 2)
        s.set(1,1)
        self.assertEqual(s.get(1,0), 0)
        self.assertEqual(s.get(1,1), 0)
        self.assertEqual(s.get(1,2), 0)
        self.assertEqual(s.get(1,3), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)