# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from sortedcontainers import *

'''
Implement a program to be used as a calendar. A new event can be added
if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty
intersection (ie some moment is common to both events).

The event can be represented as a pair of integers start and end that
represent a booking on the half-open interval [start, end), the range
of real numbers x such that start <= x < end.
'''
class MyCalendar:
    '''
    Initializes the calendar object.
    '''
    def __init__(self):
        self.dates = SortedSet()

    '''
    Returns True if the event can be added to the calendar successfully
    without causing a double booking. Otherwise return False and do not
    add the event to the calendar.
    '''
    def book(self, start: int, end: int) -> bool:
        ''' Brute force check all answers '''
        # for s,e in self.dates.items():
        #     if s < end and start < e:
        #         return False
        # self.dates[start] = end
        # return True
        '''
        Check left right of insertion point
        Based on Leetcode solution 2
        https://leetcode.com/problems/my-calendar-i/solution/
        and comment by Kakinohana
        ''''
        i = (start,end)
        if not self.dates:
            self.dates.add(i)
            return True
        # if (start,end) already present bail
        if i in self.dates:
            return False
        # check left of insertion for overlap
        p = self.dates.bisect_left(i) - 1
        # check right of insertion for overlap
        n = self.dates.bisect_right(i)
        # perform check
        if (p < 0 or self.dates[p][1] <= start) and (n == len(self.dates) or self.dates[n][0] >= end):
            self.dates.add(i)
            return True
        return False


class UnitTesting(unittest.TestCase):
    # def test_one(self):
    #     s = MyCalendar()
    #     self.assertEqual(s.book(10,20), True)
    #     self.assertEqual(s.book(15,25), False)
    #     self.assertEqual(s.book(20,30), True)
    #     self.assertEqual(s.book(20,31), False)
    #     self.assertEqual(s.book(20,21), False)

    def test_two(self):
        s = MyCalendar()
        p = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
        o = [True,True,False,False,True,False,True,True,True,False]
        for i,j in zip(p,o):
            # print(s.dates)
            # print(i,j)
            self.assertEqual(s.book(*i), j)

if __name__ == '__main__':
    unittest.main(verbosity=2)