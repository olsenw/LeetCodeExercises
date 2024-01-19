# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two lists of closed intervals, firstList and secondList, where
    firstList[i] = [starti, endi] and secondList[j] = [startj, endk]. Each list
    of intervals is pairwise disjoint and in sorted order.

    Return the intersection of these two interval lists.

    A closed interval [a,b] (with a <= b) denotes the set of real numbers x with
    a <= x <= b.

    The intersection of two closed intervals is a set of real numbers that are
    either empty or represented as a closed interval.
    '''
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        i,j = 0,0
        while i < len(firstList) and j < len(secondList):
            a,b = firstList[i]
            x,y = secondList[j]
            # if a <= x <= b <= y or x <= a <= y <= b:
            if a <= x <= b or x <= a <= y:
                answer.append([max(a,x), min(b,y)])
            if b < y:
                i += 1
            else:
                j += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,2],[5,10],[13,23],[24,25]]
        j = [[1,5],[8,12],[15,24],[25,26]]
        o = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        self.assertEqual(s.intervalIntersection(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[5,9]]
        j = []
        o = []
        self.assertEqual(s.intervalIntersection(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[3,5],[9,20]]
        j = [[4,5],[7,10],[11,12],[14,15],[16,20]]
        o = [[4,5],[9,10],[11,12],[14,15],[16,20]]
        self.assertEqual(s.intervalIntersection(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)