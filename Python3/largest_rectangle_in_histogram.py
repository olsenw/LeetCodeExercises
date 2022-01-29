# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers heights representing the historgram's bar
    height where the width of each bar is 1, return the area of the 
    largest rectangle in the histogram.
    '''
    # O(n^2) time because of rectangle checks
    # slower than a lot of other submissions...
    def largestRectangleArea(self, heights: List[int]) -> int:
        from collections import deque
        n = len(heights)
        nextSmall = [-1] * n
        # monotonic stack (decreasing)
        stack = deque()
        # start back to front
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            nextSmall[i] = stack[-1][1] if stack else n
            stack.append((heights[i],i))
        del stack
        # do rectangle checks
        best = 0
        for i in range(n):
            j = i
            while j < n:
                best = max(best, heights[j] * (nextSmall[j]-i))
                j = nextSmall[j]
        return best

    # still slow could probably improve by mixing two while together
    def largestRectangleArea_alt(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        nextSmall = [-1] * n
        stack = []
        # monotonic stack (decreasing)
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            nextSmall[i] = stack[-1][1] if stack else n
            stack.append((heights[i],i))
            # check rectangles
            j = i
            while j < n:
                best = max(best, heights[j] * (nextSmall[j]-i))
                j = nextSmall[j]
        return best
    
    # Faster solutions exist, can see them by going to the bar graph
    # and clicking on one, it will pop up with a code sample. Pretty
    # similar logic to what I got, just combined loops and, I 
    # think better ways of checking rectangles. Going to be happy with 
    # what I figured out on my own however.

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,5,6,2,3]
        o = 10
        self.assertEqual(s.largestRectangleArea(i), o)
        self.assertEqual(s.largestRectangleArea_alt(i), o)

    def test_two(self):
        s = Solution()
        i = [2,4]
        o = 4
        self.assertEqual(s.largestRectangleArea(i), o)
        self.assertEqual(s.largestRectangleArea_alt(i), o)

    def test_three(self):
        s = Solution()
        i = [3,1,2,2,2]
        o = 6
        self.assertEqual(s.largestRectangleArea(i), o)
        self.assertEqual(s.largestRectangleArea_alt(i), o)

    def test_four(self):
        s = Solution()
        i = [3,1,2,2,2,1,2]
        o = 7
        self.assertEqual(s.largestRectangleArea(i), o)
        self.assertEqual(s.largestRectangleArea_alt(i), o)

    def test_five(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 9
        self.assertEqual(s.largestRectangleArea(i), o)
        self.assertEqual(s.largestRectangleArea_alt(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)