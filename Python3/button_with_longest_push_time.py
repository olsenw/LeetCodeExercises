# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D array events which represents a sequence of events where a child
    pushes a series of buttons on a keyboard.

    Each events[i] = [indexi, timei] indicates that the button at index indexi
    was pressed at time timei.
    * The array is sorted in increasing order of time.
    * The time taken to press a button is the difference in time between
      consecutive button presses. The time for the first button is simply the
      time at which it was pressed.
    
    Return the index of the button the longest time to push. If multiple buttons
    have the same longest time, return the button with the smallest index.
    '''
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        answer = events[0][0]
        time = events[0][1]
        for i in range(len(events)-1):
            t = events[i+1][1] - events[i][1]
            if time < t or (time == t and events[i+1][0] < answer):
                time = t
                answer = events[i+1][0]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,5],[3,9],[1,15]]
        o = 1
        self.assertEqual(s.buttonWithLongestTime(i), o)

    def test_two(self):
        s = Solution()
        i = [[10,5],[1,7]]
        o = 10
        self.assertEqual(s.buttonWithLongestTime(i), o)

    def test_three(self):
        s = Solution()
        i = [[9,4],[19,5],[2,8],[3,11],[2,15]]
        o = 2
        self.assertEqual(s.buttonWithLongestTime(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)