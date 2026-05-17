# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of non-negative integers arr, start at position start. From
    index i, it is possible to jump from index i to index i + arr[i] or
    i - arr[i], check if it is possible to reach any index with value 0.

    Notice that it is not possible to jump outside the bounds of the array.
    '''
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        def dfs(index:int) -> bool:
            if index in visited:
                return False
            if index < 0 or index >= n:
                return False
            visited.add(index)
            if arr[index] == 0:
                return True
            return dfs(index - arr[index]) or dfs(index + arr[index])
        return dfs(start)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,3,0,3,1,2]
        j = 5
        o = True
        self.assertEqual(s.canReach(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,2,3,0,3,1,2]
        j = 0
        o = True
        self.assertEqual(s.canReach(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,0,2,1,2]
        j = 2
        o = False
        self.assertEqual(s.canReach(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)