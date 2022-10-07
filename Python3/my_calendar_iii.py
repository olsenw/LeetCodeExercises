# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from bisect import bisect, bisect_left

'''
A k-booking happens when k events have some non-empty intersection (i.e., there
is some time that is common to all k events.)

Given some events [start, end), after each given event, return an integer k
representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class.
'''
class MyCalendarThree_fails:
    '''
    Initializes the object.
    '''
    def __init__(self):
        # self.bookings = []
        self.starts = []
        self.ends = []
        self.k = 0

    '''
    Returns an integer k representing the largest integer such that there exits
    a k-booking in the calendar.
    '''
    # issue 1 if two same starts detect the first of the same starts
    # issue 2 long running event that covers multiple
    def book(self, start: int, end: int) -> int:
        # b = (start, -end)
        # i = bisect_left(self.bookings, b)
        # self.bookings.insert(i, b)
        # k = 0
        # while i < len(self.bookings) and self.bookings[i][0] < end:
        #     k += 1
        #     i += 1
        self.starts.insert(bisect(self.starts, start), start)
        self.ends.insert(bisect(self.ends, end), end)
        i = bisect(self.ends, start)
        j = bisect(self.starts, end-1)
        k = j - i
        if k > self.k:
            self.k = k
        return self.k

'''
inspired by leetcode hint
O(n^2) time complexity
'''
class MyCalendarThree:
    def __init__(self):
        self.events = []
    def book(self, start: int, end: int) -> int:
        self.events.insert(bisect(self.events, (start, True)), (start,True))
        self.events.insert(bisect(self.events, (end, False)), (end,False))
        k = 0
        c = 0
        for i,j in self.events:
            if j:
                c += 1
                k = max(k,c)
            else:
                c -= 1
        return k

class UnitTesting(unittest.TestCase):
    def test_one(self):
        c = MyCalendarThree()
        self.assertEqual(c.book(10,20), 1)
        self.assertEqual(c.book(50,60), 1)
        self.assertEqual(c.book(10,40), 2)
        self.assertEqual(c.book(5,15), 3)
        self.assertEqual(c.book(5,10), 3)
        self.assertEqual(c.book(25,55), 3)

    def test_two(self):
        c = MyCalendarThree()
        self.assertEqual(c.book(26,35), 1)
        self.assertEqual(c.book(26,32), 2)
        self.assertEqual(c.book(25,32), 3)
        self.assertEqual(c.book(18,26), 3)
        self.assertEqual(c.book(40,45), 3)
        self.assertEqual(c.book(19,26), 3)
        self.assertEqual(c.book(48,50), 3)
        self.assertEqual(c.book(1,6), 3)
        self.assertEqual(c.book(46,50), 3)
        self.assertEqual(c.book(11,18), 3)

    def test_three(self):
        c = MyCalendarThree()
        self.assertEqual(c.book(24,40), 1)
        self.assertEqual(c.book(43,50), 1)
        self.assertEqual(c.book(27,43), 2)
        self.assertEqual(c.book(5,21), 2)
        self.assertEqual(c.book(30,40), 3)
        self.assertEqual(c.book(14,29), 3)
        self.assertEqual(c.book(3,19), 3)
        self.assertEqual(c.book(3,14), 3)
        self.assertEqual(c.book(25,39), 4)
        self.assertEqual(c.book(6,19), 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)