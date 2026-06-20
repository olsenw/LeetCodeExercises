# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Build n new buildings in a city. The new buildings will be built in a line
    and are labeled from 1 to n.

    However, there are city restrictions on the heights of the new buildings:
    * The height of each building must be a non-negative integer.
    * The height of the first building must be 0.
    * The height difference between any two adjacent buildings cannot exceed 1.

    Additionally, there are city restrictions on the maximum height of specific
    buildings. These restrictions are given as a 2D integer array restrictions
    where restrictions[i] = [idi, maxHeighti] indicates that building idi must
    have a height less than or equal to maxHeighti.

    It is guaranteed that each building will appear at most once in
    restrictions, and building 1 will not be in restrictions.

    Return the maximum possible height of the tallest building.
    '''
    # note 2 <= n <= 10**9
    def maxBuilding_memory_limit(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions = {i:j for i,j in restrictions}
        left = [0,0]
        for i in range(2,n+1):
            left.append(left[-1] + 1)
            if i in restrictions:
                left[-1] = min(left[-1], restrictions[i])
        for i in range(n-1,0,-1):
            left[i] = min(left[i+1] + 1, left[i])
        return max(left)

    def maxBuilding_incomplete(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n,restrictions[-1][1] + n - restrictions[-1][0]])
        r = len(restrictions)
        left = [0] * (r-1)
        right = [0] * (r-1)
        for i in range(r-1):
            a,b = restrictions[i]
            x,y = restrictions[i+1]
            left[i] = b + (x-a-1)
        for i in range(r-1,0,-1):
            a,b = restrictions[i]
            x,y = restrictions[i-1]
            right[i-1] = y + (a-x-1)
        return 0

    # based on leetcode editorial
    # https://leetcode.com/problems/maximum-building-height/editorial/?envType=daily-question&envId=2026-06-20
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # prepend blocking restriction of first building
        restrictions.append([1,0])
        restrictions.sort()
        # append blocking restriction of last building
        if restrictions[-1][0] != n:
            restrictions.append([n,restrictions[-1][1] + n - restrictions[-1][0]])
        r = len(restrictions)
        # left to right limit pass
        for i in range(1,r):
            a,b = restrictions[i-1]
            x,y = restrictions[i]
            restrictions[i][1] = min(y, b + (x - a))
        # right to left limit pass
        for i in range(r-2,0,-1):
            a,b = restrictions[i]
            x,y = restrictions[i+1]
            restrictions[i][1] = min(b, y + (x - a))
        # find answer
        answer = 0
        for i in range(r-1):
            a,b = restrictions[i]
            x,y = restrictions[i+1]
            # find hill between two restrictions
            best = (x - a + b + y) // 2
            answer = max(answer, best)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[2,1],[4,1]]
        o = 2
        self.assertEqual(s.maxBuilding(i,j), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = []
        o = 5
        self.assertEqual(s.maxBuilding(i,j), o)

    def test_three(self):
        s = Solution()
        i = 10
        j = [[5,3],[2,5],[7,4],[10,3]]
        o = 5
        self.assertEqual(s.maxBuilding(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)