# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import OrderedDict, defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

To determine the least frequently used key, a use counter is maintained for each
key in the cache. The key with the smallest use counter is the least frequently
used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to 
the put operation). The use counter for a key in the cache is incremented either
a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
'''
# incorrect, while loop in move left prevents O(1) behavior
class LFUCache_invalid:
    '''
    Initializes the object with the capacity of the data structure.
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict() # key to [value, frequency, index]
        self.cache = list() # keys ordered by frequency

    '''
    here is problem for tle...
    need better insert
    actual use of linked list instead of moving
    '''
    def _moveLeft(self, key):
        index = self.map[key][2]
        if index and self.map[key][1] >= self.map[self.cache[index - 1]][1]:
            self.map[self.cache[index - 1]][2] += 1
            self.map[key][2] -= 1
            self.cache[index - 1], self.cache[index] = self.cache[index], self.cache[index - 1]
            # recursive...?
            self._moveLeft(key)

    '''
    Gets the value of the key if the key exists in the cache. Otherwise returns
    -1.
    '''
    def get(self, key: int) -> int:
        # no space
        if not self.capacity:
            return -1
        if key in self.map:
            self.map[key][1] += 1
            self._moveLeft(key)
            return self.map[key][0]
        return -1

    '''
    Update the value of the key if present, or inserts the key if not already
    present. When the cache reaches its capacity, it should invalidate and
    remove the least frequently used key before inserting a new item. If there
    is a tie (ie two or more keys with the same frequency), the least recently
    used key would be invalidated.
    '''
    def put(self, key: int, value: int) -> None:
        # no space
        if not self.capacity:
            return
        # update
        if key in self.map:
            self.map[key][0] = value
            self.map[key][1] += 1
            self._moveLeft(key)
        # trivial add
        elif len(self.cache) < self.capacity:
            self.map[key] = [value, 1, len(self.cache)]
            self.cache.append(key)
            self._moveLeft(key)
        # remove add
        else:
            del self.map[self.cache[-1]]
            self.map[key] = [value, 1, self.capacity - 1]
            self.cache[-1] = key
            self._moveLeft(key)

# based on solution by eroneko
# https://leetcode.com/problems/lfu-cache/solutions/718724/python-solution-with-ordereddict/?orderBy=most_votes&languageTags=python3
# the only reason Ordered Dict works (ie O(1) requirement) is being used as
# double linked list (in solution and actual implementation)
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = defaultdict(int) # key -> frequency
        self.frequency = defaultdict(OrderedDict) # frequency -> {key -> val}
        self.least = 0 # minimum used frequency of keys

    # update the data structure and return latest value
    def updateFrequency(self, key: int, value: int = None) -> int:
        f = self.items[key]
        v = self.frequency[f].pop(key)
        # neat way to conditionally update a value
        if value is not None:
            v = value
        self.frequency[f+1][key] = v # add key to updated frequency
        self.items[key] += 1 # update frequency in the items
        # update minimum frequency
        if self.least == f and not self.frequency[f]:
            self.least += 1
        return v

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        return self.updateFrequency(key)

    def put(self, key: int, value: int) -> None:
        # zero capacity (ie unable to store any values)
        if not self.capacity:
            return
        # update existing item
        elif key in self.items:
            self.updateFrequency(key, value)
        else:
            # cache full - remove item
            if len(self.items) == self.capacity:
                self.items.pop(self.frequency[self.least].popitem(last=False)[0])
            # insert key
            self.least = 1
            self.items[key] = 1
            self.frequency[1][key] = value

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = LFUCache(2)
        s.put(1,1)
        s.put(2,2)
        self.assertEqual(s.get(1), 1)
        s.put(3,3)
        self.assertEqual(s.get(2), -1)
        self.assertEqual(s.get(3), 3)
        s.put(4,4)
        self.assertEqual(s.get(1), -1)
        self.assertEqual(s.get(3), 3)
        self.assertEqual(s.get(4), 4)

    def test_two(self):
        s = LFUCache(0)
        s.put(1,1)
        self.assertEqual(s.get(1), -1)

    def test_three(self):
        s = LFUCache(3)
        s.put(1,1)
        s.put(2,2)
        s.put(3,3)
        s.put(4,4)
        self.assertEqual(s.get(4), 4)
        self.assertEqual(s.get(3), 3)
        self.assertEqual(s.get(2), 2)
        self.assertEqual(s.get(1), -1)
        s.put(5,5)
        self.assertEqual(s.get(1), -1)
        self.assertEqual(s.get(2), 2)
        self.assertEqual(s.get(3), 3)
        self.assertEqual(s.get(4), -1)
        self.assertEqual(s.get(5), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)