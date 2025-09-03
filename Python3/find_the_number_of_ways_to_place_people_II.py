# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

class Solution:
    '''
    Given a 2D array points of size n x 2 representing integer coordinates of
    some points on a 2S-plane, where points[i] = [xi, yi].
    
    Place n people, including Alice and Bob, at these points such that there is
    exactly one person at every point. Alice wants to be alone with Bob, so
    Alice will build a rectangular fence with Alice's position as the upper left
    corner and Bob's position as the lower right corner of the fence (Note that
    the fence might not enclose any area, ie it can be a line). If any person
    other than Alice and Bob is either inside the fence or on the fence, Alice
    will be sad.

    Return the number of pairs of points where Alice and Bob can be placed such
    that Alice does not become sad on building the fence.
    '''
    # solution from previous version of problem
    # https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description/?envType=daily-question&envId=2025-09-02
    # encounters a time limit exceeded error
    def numberOfPairs_tle(self, points: List[List[int]]) -> int:
        def test(x:Tuple[int,int], y:Tuple[int,int], point:Tuple[int,int]) -> bool:
            if x[0] <= point[0] <= y[0]:
                return y[1] <= point[1] <= x[1]
            return False
        answer = 0
        points.sort(key=lambda x: (x[0],-x[1]))
        for i,x in enumerate(points):
            for j,y in enumerate(points[i+1:], i+1):
                # if not any(test(x,y,z) for k,z in enumerate(points[i+1:j], i+1)):
                #     answer += 1
                if x[1] < y[1]:
                    continue
                yes = 1
                for k,z in enumerate(points[i+1:j],i+1):
                    if test(x,y,z):
                        yes = 0
                        break
                answer += yes
        return answer

    def numberOfPairs(self, points: List[List[int]]) -> int:
        answer = 0
        points.sort(key=lambda x: (x[0], -x[1]))
        for i,x in enumerate(points):
            lowerLimit = float('-inf')
            for j,y in enumerate(points[i+1:], i+1):
                # out of bounds to build fence
                if x[1] < y[1]:
                    continue
                # previous point in the bounds
                if y[1] <= lowerLimit:
                    continue
                # new possible point
                answer += 1
                lowerLimit = y[1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[2,2],[3,3]]
        o = 0
        self.assertEqual(s.numberOfPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [[6,2],[4,4],[2,6]]
        o = 2
        self.assertEqual(s.numberOfPairs(i), o)

    def test_three(self):
        s = Solution()
        i = [[3,1],[1,3],[1,1]]
        o = 2
        self.assertEqual(s.numberOfPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)