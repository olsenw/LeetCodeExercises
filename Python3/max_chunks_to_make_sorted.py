# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        answer = 0
        a = sorted(arr)
        def chunk(i):
            x,y = set(), set()
            for i in range(i, len(arr)):
                x.add(arr[i])
                y.add(a[i])
                if x == y:
                    return i + 1
            return len(arr)
        i = 0
        while i < len(arr):
            i = chunk(i)
            answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,3,2,1,0]
        o = 1
        self.assertEqual(s.maxChunksToSorted(i), o)

    def test_two(self):
        s = Solution()
        i = [1,0,2,3,4]
        o = 4
        self.assertEqual(s.maxChunksToSorted(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)