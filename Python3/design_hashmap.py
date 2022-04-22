# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Design a HashMap without using any built in hash table libraries.
'''
# one giant list with a default value for every key
class MyHashMap_Brute:
    '''
    Initializes the object with an empty map.
    '''
    def __init__(self):
        self.values = [-1] * (10**6 + 1)

    '''
    Inserts a (key, value) pair into the HashMap. If the key already
    exists in th map, update the corresponding value
    '''
    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    '''
    Returns the value to which the specified key is mapped or -1 if this
    map contains no mapping for the key.
    '''
    def get(self, key: int) -> int:
        return self.values[key]

    '''
    Removes the key and its corresponding value if the map contains the
    mapping for the key.
    '''
    def remove(self, key: int) -> None:
        self.values[key] = -1

# makes use of buckets and list for collision, stores mappings as tuples
class MyHashMap:

    def __init__(self, buckets=1024):
        self.buckets = [[] for _ in range(buckets)]

    def hash(self, key):
        return key % len(self.buckets)

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        p = (key, value)
        for i, (j, _) in enumerate(self.buckets[h]):
            if j == key:
                self.buckets[h][i] = p
                return
        self.buckets[h].append(p)

    def get(self, key: int) -> int:
        h = self.hash(key)
        for i, j in self.buckets[h]:
            if i == key:
                return j
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        for i, (j, _) in enumerate(self.buckets[h]):
            if j == key:
                del self.buckets[h][i]
                return

class UnitTesting(unittest.TestCase):
    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)

    def test_one(self):
        s = MyHashMap()
        s.put(1,1)
        s.put(2,2)
        self.assertEqual(s.get(1), 1)
        self.assertEqual(s.get(3), -1)
        s.put(2,1)
        self.assertEqual(s.get(2), 1)
        s.remove(2)
        self.assertEqual(s.get(2), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)