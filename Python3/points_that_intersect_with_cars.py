# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D integer array nums representing the coordinates of the
    cars parking on a number line. For any index i, nums[i] = [starti, endi]
    where start i is the starting point of the ith car and endi is the ending
    point of the ith car.

    Return the number of integer points on the line that are covered with any
    part of a car.
    '''
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        answer = -1
        nums.sort()
        start = 0
        end = 0
        car = 0
        while car < len(nums):
            i,j = nums[car]
            if start <= i <= end:
                end = max(end, j)
            else:
                answer += end - start + 1
                start = i
                end = j
            car += 1
        return answer + end - start + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,6],[1,5],[4,7]]
        o = 7
        self.assertEqual(s.numberOfPoints(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[5,8]]
        o = 7
        self.assertEqual(s.numberOfPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)