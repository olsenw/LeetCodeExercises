# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers red and blue representing the count of red and blue
    colored balls. Arrange these balls to form a triangle such that the 1st row
    will have 1 ball, the 2nd row will have 2 balls, the 3rd row will have 3
    balls, and so on.

    All the balls in a particular row should be the same color, and adjacent
    rows should have different colors.

    Return the maximum height of the triangle that can be achieved.
    '''
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def take(a,b):
            answer = 0
            row = 1
            while a >= row:
                answer += 1
                a -= row
                row += 1
                if b < row:
                    break
                answer += 1
                b -= row
                row += 1
            return answer
        return max(take(red, blue), take(blue,red))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2,4
        o = 3
        self.assertEqual(s.maxHeightOfTriangle(*i), o)

    def test_two(self):
        s = Solution()
        i = 2,1
        o = 2
        self.assertEqual(s.maxHeightOfTriangle(*i), o)

    def test_three(self):
        s = Solution()
        i = 1,1
        o = 1
        self.assertEqual(s.maxHeightOfTriangle(*i), o)

    def test_four(self):
        s = Solution()
        i = 10,1
        o = 2
        self.assertEqual(s.maxHeightOfTriangle(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)