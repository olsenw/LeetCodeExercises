# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
from math import gcd
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    
    Given an array points where points[i] = [xi, xj] represents a point on the
    X-Y plane, return the maximum number of points that lie on the same straight
    line.
    '''
    # O(n^3) time
    # floating point precision issues in equation solving
    def maxPoints_brute_fails(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        answer = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                found = 0
                # y = m x + b
                x1, y1 = points[i]
                x2, y2 = points[j]
                # test vertical line
                if x1 == x2:
                    for x,_ in points:
                        if x == x1:
                            found += 1
                else:
                    # m = (y2 - y1) / (x2 - x1)
                    m = (y2 - y1) / (x2 - x1)
                    # b = y - m x
                    b = y2 - m * x2
                    for x,y in points:
                        if y == m * x + b:
                            found += 1
                        pass
                answer = max(found, answer)
        return answer

    def maxPoints(self, points: List[List[int]]) -> int:
        # trivial case
        if len(points) == 1:
            return 1
        # answer = Counter()
        answer = 0
        for i in range(len(points)):
            alt = Counter()
            # for j in range(i + 1, len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                a = y2 - y1
                b = x2 - x1
                c = y1 * x2 - x1 * y2
                d = gcd(a, gcd(b,c))
                # answer[(a // d, b // d, c // d)] += 1
                alt[(a // d, b // d, c // d)] += 1
            answer = max(answer, max(alt.values()))
        # return max(answer.values())
        return answer + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[2,2],[3,3]]
        o = 3
        self.assertEqual(s.maxPoints(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        o = 4
        self.assertEqual(s.maxPoints(i), o)

    def test_two_two(self):
        s = Solution()
        i = [[3,2],[4,1],[2,3],[1,4]]
        o = 4
        self.assertEqual(s.maxPoints(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1],[1,2],[1,3],[2,2]]
        o = 3
        self.assertEqual(s.maxPoints(i), o)

    def test_four(self):
        s = Solution()
        i = [[-6,-1],[3,1],[12,3]]
        o = 3
        self.assertEqual(s.maxPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)