# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    There are n different online courses numbered from 1 to n. Given an
    array courses where courses[i] = [durationi, lastDayi] indicates
    that the ith course should be taken continuously for durationi days
    and must be finished before or on lastDayi.

    Start on the 1st day and no more than one course can be taken for at
    a time.

    Return the maximum number of courses that can be taken.
    '''
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        h = [0]
        t = 0
        # for d,e in sorted((c for c in courses if c[0] <= c[1]), key=lambda x: (x[1],-x[0])):
        for d,e in sorted(courses, key=lambda x: (x[1],-x[0])):
            # can just add course
            if t + d <= e:
                heapq.heappush(h, -d)
                t += d
            # see if swap with previously largest course
            elif h[0] + d < 0 and t + h[0] + d <= e:
                t += heapq.heapreplace(h, -d)
                t += d
        return len(h) - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[100,200],[200,1300],[1000,1250],[2000,3200]]
        o = 3
        self.assertEqual(s.scheduleCourse(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2]]
        o = 1
        self.assertEqual(s.scheduleCourse(i), o)

    def test_three(self):
        s = Solution()
        i = [[3,2],[4,3]]
        o = 0
        self.assertEqual(s.scheduleCourse(i), o)

    def test_four(self):
        s = Solution()
        i = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
        o = 4
        self.assertEqual(s.scheduleCourse(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)