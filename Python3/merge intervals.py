# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of intervals where intervals[i] = [si, ei] merge all
    overlapping intervals and return an array of the non-overlapping
    intervals that cover all the intervals in the input.
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # create dictionary of intervals
        d = {}
        for s,e in intervals:
            # combines intervals with the same start
            d[s] = max(d.get(s,0), e)
        # sort dictionary by keys (because keys are ordered by insertion)
        d = dict(sorted(d.items()))
        # combine intervals with overlapping start/end
        l = []
        i = iter(d.items())
        start, end = next(i)
        for s, e in i:
            if s <= end:
                # extend interval
                end = max(end, e)
            else:
                l.append([start, end])
                start, end = s, e
        l.append([start,end])
        return l

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        i = [[1,3],[2,6],[8,10],[15,18]]
        m = [[1,6],[8,10],[15,18]]
        self.assertEqual(s.merge(i), m)

    def test_two(self):
        s = Solution()
        i = [[1,4],[4,5]]
        m = [[1,5]]
        self.assertEqual(s.merge(i), m)

    def test_three(self):
        s = Solution()
        i = [[2,2]]
        m = [[2,2]]
        self.assertEqual(s.merge(i), m)

    def test_four(self):
        s = Solution()
        i = [[1,2],[2,2],[1,3],[2,4],[5,6],[5,7]]
        m = [[1,4],[5,7]]
        self.assertEqual(s.merge(i), m)

    def test_five(self):
        s = Solution()
        i = [[1,4],[0,4]]
        m = [[0,4]]
        self.assertEqual(s.merge(i), m)

    def test_six(self):
        s = Solution()
        i = [[1,4],[2,3]]
        m = [[1,4]]
        self.assertEqual(s.merge(i), m)

if __name__ == '__main__':
    unittest.main(verbosity=2)