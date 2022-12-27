# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n bags numbered from 0 to n - 1. Given two 0-indexed integer
    arrays capacity and rocks. The ith bag can hold a maximum of capacity[i]
    rocks and currently contains rocks[i] rocks. There is also given an integer
    additional rocks, which is the number of additional rocks that can be placed
    in any bag.

    Return the maximum number of bags that could have full capacity after
    placing the additional rocks in some bags.
    '''
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        answer = 0
        fill = sorted(c - r for c, r in zip(capacity,rocks))
        for f in fill:
            if f <= additionalRocks:
                additionalRocks -= f
                answer += 1
            else:
                break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,4,5]
        j = [1,2,4,4]
        k = 2
        o = 3
        self.assertEqual(s.maximumBags(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [10,2,2]
        j = [2,2,0]
        k = 100
        o = 3
        self.assertEqual(s.maximumBags(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)