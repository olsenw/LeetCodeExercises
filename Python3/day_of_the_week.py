# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a date, return the corresponding day of the week for that date.

    The input is given as three integers representing the day, month and year
    respectively.

    Return the answer as one of the following values {"Sunday", "Monday",
    "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

    Note January 1, 1971 was a friday.
    '''
    
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def isLeapYear(year:int) -> bool:
            if year % 4 == 0:
                if year % 400 == 0:
                    return True
                if year % 100 != 0:
                    return True
            return False
        def daysInYear(year:int) -> int:
            if isLeapYear(year):
                return 366
            return 365
        def daysToMonth(month:int, leap:bool) -> int:
            months = {1:31,
                      2:28, # 29 on a leap year
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}
            answer = sum(months[i] for i in range(1,month))
            return answer + 1 if leap and month > 2 else answer
        def daysToWeekday(days:int) -> str:
            weekdays = {0:"Friday",
                        1:"Saturday",
                        2:"Sunday",
                        3:"Monday",
                        4:"Tuesday",
                        5:"Wednesday",
                        6:"Thursday"}
            return weekdays[days % 7]
        # answer = sum(daysInYear(y) for y in range(1971, year))
        answer = 0
        for y in range(1971, year):
            d = daysInYear(y)
            l = isLeapYear(y)
            answer += d
        leap = isLeapYear(year)
        answer += daysToMonth(month, leap)
        answer += day - 1
        answer = daysToWeekday(answer)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 31
        j = 8
        k = 2019
        o = "Saturday"
        self.assertEqual(s.dayOfTheWeek(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 18
        j = 7
        k = 1999
        o = "Sunday"
        self.assertEqual(s.dayOfTheWeek(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 15
        j = 8
        k = 1993
        o = "Sunday"
        self.assertEqual(s.dayOfTheWeek(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 1
        j = 1
        k = 1971
        o = "Friday"
        self.assertEqual(s.dayOfTheWeek(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = 28
        j = 5
        k = 2026
        o = "Thursday"
        self.assertEqual(s.dayOfTheWeek(i,j,k), o)

    def test_six(self):
        s = Solution()
        i = 29
        j = 2
        k = 2016
        o = "Monday"
        self.assertEqual(s.dayOfTheWeek(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)