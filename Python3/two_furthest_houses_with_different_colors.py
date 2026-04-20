# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n houses evenly lined up on the street, and each house is
    beautifully painted. Given a 0-indexed integer array colors of length n,
    where colors[i] represents the color of the ith house.

    Return the maximum distance between two houses with different colors.

    The distance between the ith and jth houses is abs(i - j), where abs(x) is
    the absolute value of x.
    '''
    def maxDistance(self, colors: List[int]) -> int:
        # [color, index]
        a = None
        b = None
        answer = 0
        for i in range(len(colors)):
            if a is None:
                a = [colors[i], i]
            elif b is None and colors[i] != a[0]:
                b = [colors[i], i]
                answer = max(answer, b[1] - a[1])
            elif b is None:
                continue
            elif colors[i] != a[0]:
                answer = max(answer, i - a[1])
            else:
                answer = max(answer, i - b[1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,6,1,1,1]
        o = 3
        self.assertEqual(s.maxDistance(i), o)

    def test_two(self):
        s = Solution()
        i = [1,8,3,8,3]
        o = 4
        self.assertEqual(s.maxDistance(i), o)

    def test_three(self):
        s = Solution()
        i = [0,1]
        o = 1
        self.assertEqual(s.maxDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)