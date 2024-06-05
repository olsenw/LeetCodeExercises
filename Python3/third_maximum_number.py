# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the third distinct maximum number in
    this array. If the third maximum does not exist, return the maximum number.
    '''
    def thirdMax(self, nums: List[int]) -> int:
        h = []
        for n in nums:
            if n not in h:
                if len(h) < 3:
                    heapq.heappush(h, n)
                else:
                    heapq.heappushpop(h, n)
        return max(h) if len(h) < 3 else h[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,1]
        o = 1
        self.assertEqual(s.thirdMax(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        o = 2
        self.assertEqual(s.thirdMax(i), o)

    def test_three(self):
        s = Solution()
        i = [2,2,3,1]
        o = 1
        self.assertEqual(s.thirdMax(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)