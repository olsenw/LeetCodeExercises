# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedDict, SortedList, SortedSet

'''
Implement a program to use as a calendar. An event can be added if the event
does not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (ie,
some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents
a booking on the half-open interval [start, end), the range of real numbers x
such that start <= x < end.

Implement the MyCalendarTwo class:
'''
class MyCalendarTwo_Fails:
    '''
    Initializes the calendar object.
    '''
    def __init__(self):
        self.first = SortedDict()
        self.double = SortedDict()
        return

    '''
    Returns true if the event can be added to the calendar successfully without
    causing a triple booking. Otherwise, return false and do not add the event
    to the calendar.
    '''
    def book(self, start: int, end: int) -> bool:
        i = self.double.bisect_left(start)
        while i < len(self.double):
            j = self.double.keys()[i]
            if start <= j < end:
                return False
            i += 1
        i = self.first.bisect_left(start)
        while i < len(self.first):
            j = self.first.keys()[i]
            if start <= j < end:
                a,b = j, self.first[j]
                del(self.first[j])
                if start < a:
                    self.first[start] = a
                self.double[a] = min(b, end)
                if b != end:
                    self.first[min(b, end)] = max(b, end)
                pass
            else:
                break
            i += 1
        self.first[start] = end
        return True

class MyCalendarTwo_fail2:
    def __init__(self):
        self.single = SortedList()
        self.double = SortedList()
        # self.single = SortedSet()
        # self.double = SortedSet()

    def book(self, start: int, end: int) -> bool:
        # date = (start, end)
        # if date in self.double:
        #     return False
        # i = self.double.bisect_left(date) - 1
        # j = self.double.bisect_right(date)
        # if not ((i < 0 or self.double[i][1] <= start) and (j == len(self.double) or self.double[j][0] >= end)):
        #     return False
        # if date in 
        # return True
        i = self.double.bisect_left([start,start])
        j = self.double.bisect_right([end,end])
        if i < j:
            for k in range(i, j):
                a,b = self.double[k]
                if start <= a < end or a <= start < b:
                    return False
        i = self.single.bisect_left([start,start])
        j = self.single.bisect_right([end,end])
        if i == j:
            self.single.add([start,end])
            return True
        for k in range(i, j):
            a,b = self.single[k]
            if start <= a < end:
                del(self.single[k])
                if start < a:
                    self.single.add([start,a])
                self.double.add([a, min(b,end)])
                if b != end:
                    self.single.add([min(b,end), max(b,end)])
            elif a < start < b:
                del(self.single[k])
                self.single.add([a,start])
                self.double.add([start, min(b,end)])
                if b != end:
                    self.single.add([min(b,end), max(b,end)])
        return True

# based on LeetCode editorial
# https://leetcode.com/problems/my-calendar-ii/?envType=daily-question&envId=2024-09-27
class MyCalendarTwo:
    def __init__(self):
        self.booking = []
        self.overlap = []

    def isOverlap(a:int,b:int,x:int,y:int) -> bool:
        return max(a,x) < min(b,y)

    def getOverlap(a:int,b:int,x:int,y:int) -> list[int]:
        return [max(a,x), min(b,y)]

    def book(self, start: int, end: int) -> bool:
        for i,j in self.overlap:
            if MyCalendarTwo.isOverlap(start, end, i, j):
                return False
        for i,j in self.booking:
            if MyCalendarTwo.isOverlap(start, end, i, j):
                self.overlap.append(MyCalendarTwo.getOverlap(start, end, i, j))
        self.booking.append([start, end])
        return True

'''
LeetCode also has a neat line scan method
'''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = MyCalendarTwo()
        self.assertEqual(s.book(10, 20), True)
        self.assertEqual(s.book(50, 60), True)
        self.assertEqual(s.book(10, 40), True)
        self.assertEqual(s.book(5, 15), False)
        self.assertEqual(s.book(5, 10), True)
        self.assertEqual(s.book(25, 55), True)

    def test_two(self):
        s = MyCalendarTwo()
        self.assertEqual(s.book(24, 40), True)
        self.assertEqual(s.book(43, 50), True)
        self.assertEqual(s.book(27, 43), True)
        self.assertEqual(s.book(5, 21), True)
        self.assertEqual(s.book(30, 40), False)
        self.assertEqual(s.book(14, 29), False)
        self.assertEqual(s.book(3, 19), True)
        self.assertEqual(s.book(3, 14), False)
        self.assertEqual(s.book(25, 39), False)
        self.assertEqual(s.book(6, 19), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)