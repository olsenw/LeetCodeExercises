# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from sortedcontainers import SortedSet

'''
Given a data stream input of non-negative integers a1,a2,...,a3, summarize the
numbers seen so far as a list of disjoint intervals.
'''
class SummaryRanges:
    '''
    Initializes the object with an empty stream.
    '''
    def __init__(self):
        self.s = SortedSet()

    '''
    Adds the integer value to the stream.
    '''
    def addNum(self, value: int) -> None:
        self.s.add(value)

    '''
    Returns a summary of the integers in the stream currently as a list of
    disjoint intervals [starti, endi]. The answer should be sorted by starti.
    '''
    def getIntervals(self) -> List[List[int]]:
        if not self.s:
            return []
        answer = []
        s = e = self.s[0]
        for n in self.s:
            if n > e + 1:
                answer.append([s,e])
                s = n
            e = n
        answer.append([s,e])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = SummaryRanges()
        s.addNum(1)
        self.assertEqual(s.getIntervals(), [[1,1]])
        s.addNum(3)
        self.assertEqual(s.getIntervals(), [[1, 1], [3, 3]])
        s.addNum(7)
        self.assertEqual(s.getIntervals(), [[1, 1], [3, 3], [7, 7]])
        s.addNum(2)
        self.assertEqual(s.getIntervals(), [[1, 3], [7, 7]])
        s.addNum(6)
        self.assertEqual(s.getIntervals(), [[1, 3], [6, 7]])

if __name__ == '__main__':
    unittest.main(verbosity=2)