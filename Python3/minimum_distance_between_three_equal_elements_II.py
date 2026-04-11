# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(list)
        answer = 3 * n
        for i in range(n):
            d[nums[i]].append(i)
        for i in d:
            for j in range(1,len(d[i])-1):
                a,b,c = d[i][j-1], d[i][j], d[i][j+1]
                answer = min(answer, abs(a-b) + abs(b-c) + abs(c-a))
        return answer if answer < 3 * n else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1,1,3]
        o = 6
        self.assertEqual(s.minimumDistance(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,3,2,1,2]
        o = 8
        self.assertEqual(s.minimumDistance(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = -1
        self.assertEqual(s.minimumDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)