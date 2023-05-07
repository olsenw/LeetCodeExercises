# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedDict, SortedList

class Solution:
    '''
    Given a 0-indexed integer array of obstacles of length n, where obstacles[i]
    describes the height of the ith obstacle.

    For every index i between 0 and n-1 (inclusive), find the length of the
    longest obstacle course in obstacles such that:
    * It is possible to choose any number of obstacles between 0 and i
      inclusive.
    * The ith obstacle must be included in the course.
    * The chosen obstacles must have the same order as they appear in obstacles.
    * Every obstacle (except the first) is taller than or the same height as the
      obstacles immediately before it.
    
    Return an array ans of length n, where ans[i] is the length of the longest
    obstacle course for index i as described above.
    '''
    # unsure how to use sorteddict correctly
    def longestObstacleCourseAtEachPosition_broken(self, obstacles: List[int]) -> List[int]:
        answer = [1]
        sd = SortedDict()
        sd[obstacles[0]] = 1
        for i in range(1, len(obstacles)):
            h = obstacles[i]
            j = sd.bisect_right(h)
            if j < len(sd):
                k = sd.keys()[j]
                sd[h] = sd[k] + 1
            else:
                sd[h] = 1
            answer.append(sd[h])
        return answer

    # closer but not right
    def longestObstacleCourseAtEachPosition_fails(self, obstacles: List[int]) -> List[int]:
        answer = [1]
        d = {obstacles[0]:1}
        l = SortedList([obstacles[0]])
        for i in range(1,len(obstacles)):
            h = obstacles[i]
            k = l.bisect_left(h)
            if h in d:
                if k > 0:
                    d[h] = max(d[h], d[l[k-1]]) + 1
                else:
                    d[h] += 1
            else:
                if k == 0 and l[k] > h:
                    d[h] = 1
                elif k == len(l) or l[k] > h:
                    d[h] = d[l[k-1]] + 1
                else:
                    d[h] = d[l[k]] + 1
                l.add(h)
            answer.append(d[h])
        return answer

    # the leetcode solution for this problem
    # https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/editorial/
    # above I was attempting to track the final obstacle and correlate it to length
    # here the length is correlated to final element in sequence
    def longestObstacleCourseAtEachPosition_leetcode(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        answer = [1] * n
        
        # lis[i] records the lowest increasing sequence of length i + 1.
        lis = []
    
        for i, height in enumerate(obstacles):
            # Find the rightmost insertion position idx.
            idx = bisect.bisect_right(lis, height)
            
            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height
            answer[i] = idx + 1
            
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,2]
        o = [1,2,3,3]
        self.assertEqual(s.longestObstacleCourseAtEachPosition(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,1]
        o = [1,2,1]
        self.assertEqual(s.longestObstacleCourseAtEachPosition(i), o)

    def test_three(self):
        s = Solution()
        i = [3,1,5,6,4,2]
        o = [1,1,2,3,2,2]
        self.assertEqual(s.longestObstacleCourseAtEachPosition(i), o)

    def test_four(self):
        s = Solution()
        i = [5,1,5,5,1,3,4,5,1,4]
        o = [1,1,2,3,2,3,4,5,3,5]
        self.assertEqual(s.longestObstacleCourseAtEachPosition(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)