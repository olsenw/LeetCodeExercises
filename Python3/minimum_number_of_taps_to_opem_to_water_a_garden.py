# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        answer = 1
        r = sorted([max(0,i - ranges[i]), i + ranges[i]] for i in range(n+1) if ranges[i] > 0)
        t = 0
        a,b = r[0]
        while r[t][0] == a:
            if r[t][1] > b:
                b = r[t][1]
            t += 1
        while t < n + 1:
            if r[t][0] >=
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [3,4,1,1,0,0]
        o = 1
        self.assertEqual(s.minTaps(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [0,0,0,0]
        o = -1
        self.assertEqual(s.minTaps(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)