# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Winter is coming! During the contest design a standard heater with a fixed
    warm radius to warm all the houses.

    Every house can be warmed, as long as the house is within the heater's warm
    radius range.

    Given the positions of houses and heaters on a horizontal line, return the
    minimum radius standard of heaters so that those heaters could cover all
    houses.

    Notice that all the heaters follow the radius standard, and the warm radius
    will be the same.
    '''
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def test(r):
            j = 0
            for i in range(len(houses)):
                while j < len(heaters) - 1 and abs(houses[i] - heaters[j]) > r:
                    j += 1
                if abs(houses[i] - heaters[j]) > r:
                    return False
            return True
        # sort houses and heaters
        houses.sort()
        heaters.sort()
        # binary search to find the minimum distance
        i,j = 0, max(houses[-1], heaters[-1])
        while i < j:
            k = i + (j - i) // 2
            if test(k):
                j = k
            else:
                i = k + 1
        return i

    # sample 229ms submission
    # two linear passes to find longest distance from house and heater
    def findRadius_online(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        M = len(houses)
        N = len(heaters)
        res=[float(('inf'))]*M
        i,j=0,0
        while i < M and j < N:
            if houses[i] <= heaters[j]:
                res[i] = heaters[j] - houses[i]
                i += 1
            else:
                j += 1
        i = M-1
        j = N-1
        while i>=0 and j >= 0:
            if houses[i] >= heaters[j]:
                res[i] = min(res[i], houses[i] - heaters[j])
                i-=1
            else:
                j-=1
        return max(res)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = [2]
        o = 1
        self.assertEqual(s.findRadius(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        j = [1,4]
        o = 1
        self.assertEqual(s.findRadius(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,5]
        j = [2]
        o = 3
        self.assertEqual(s.findRadius(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3]
        j = [1,2,3]
        o = 0
        self.assertEqual(s.findRadius(i,j), o)

    def test_five(self):
        s = Solution()
        i = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
        j = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
        o = 161834419
        self.assertEqual(s.findRadius(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)