# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from sortedcontainers import SortedDict

'''
Design a time-based key-value data structure that can store multiple values for
the same key at different time stamps and retrieve the key's value at a certain
timestamp.

Implement the TimeMap class:
'''
class TimeMap:
    '''
    Initializes the object of the data structure.
    '''
    def __init__(self):
        self.h = dict()

    '''
    Stores the key with the value at the given time timestamp.
    '''
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.h:
            self.h[key][timestamp] = value
        else:
            self.h[key] = SortedDict({timestamp: value})

    '''
    Returns a value such that set was called previously, with
    timestamp_prev <= timestamp. If there are multiple such values, it returns
    the value associated with the largest timestamp_prev. If there are no
    values, it returns "".
    '''
    def get(self, key: str, timestamp: int) -> str:
        if key in self.h:
            i = self.h[key].bisect(timestamp) - 1
            a, b = self.h[key].peekitem(i)
            if a <= timestamp:
                return b
        return ""

class UnitTesting(unittest.TestCase):
    def test_one(self):
        t = TimeMap()
        t.set("foo","bar",1)
        self.assertEqual(t.get("foo", 1), "bar")
        self.assertEqual(t.get("foo", 3), "bar")
        t.set("foo","barbar",4)
        self.assertEqual(t.get("foo", 4), "barbar")
        self.assertEqual(t.get("foo", 5), "barbar")

if __name__ == '__main__':
    unittest.main(verbosity=2)