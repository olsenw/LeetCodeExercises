# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n rooms labeled from 0 o n - 1 and all the rooms are locked except
    for room 0. The goal is to visit all the rooms. However a room cannot be
    entered without the corresponding key.

    When a room is visited, it is possible to a set of distinct keys. Each key
    has a number on it, denoting which room it unlocks. It is possible to take
    all keys from a given room.

    Given an array rooms where rooms[i] is the set of keys that can be obtained
    by visiting room i, return true if it is possible to visit all the rooms, or
    false otherwise.
    '''
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        keys = set()
        check = set([0])
        while check:
            r = check.pop()
            keys.add(r)
            for k in rooms[r]:
                if k not in keys:
                    check.add(k)
        return len(keys) == n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1],[2],[3],[]]
        o = True
        self.assertEqual(s.canVisitAllRooms(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[3,0,1],[2],[0]]
        o = False
        self.assertEqual(s.canVisitAllRooms(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)