# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Design a HashSet without using any built-in hash table libraries.
'''
# most brute force solution possible have a checklist of every possible
# value that can be in the set
class MyHashSet_brute:

    def __init__(self):
        self.buckets = [False] * (10 ** 6 + 1)

    '''
    Inserts the value key into the HashSet
    '''
    def add(self, key: int) -> None:
        self.buckets[key] = True

    '''
    Removes the value key in the HashSet. If key does not exist in the
    HashSet do nothing.
    '''
    def remove(self, key: int) -> None:
        self.buckets[key] = False

    '''
    Returns whether the value key exists in the HashSet or not.
    '''
    def contains(self, key: int) -> bool:
        return self.buckets[key]

# fixed number of buckets using list for hash collion resolution
class MyHashSet:

    def __init__(self, buckets = 1024):
        self.buckets = [[] for _ in range(buckets)]

    def hash(self, key):
        return key % len(self.buckets)

    def add(self, key: int) -> None:
        h = self.hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self.hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self.hash(key)]

class UnitTesting(unittest.TestCase):
    # Your MyHashSet object will be instantiated and called as such:
    # obj = MyHashSet()
    # obj.add(key)
    # obj.remove(key)
    # param_3 = obj.contains(key)

    def test_one(self):
        s = MyHashSet()
        s.add(1)
        s.add(2)
        self.assertEqual(s.contains(1), True)
        self.assertEqual(s.contains(3), False)
        s.add(2)
        self.assertEqual(s.contains(2), True)
        s.remove(2)
        self.assertEqual(s.contains(2), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)