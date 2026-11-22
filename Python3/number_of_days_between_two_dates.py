# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Write a program to count the number of days between two dates.

    The two dates are given as strings, their format is YYYY-MM-DD as shown in
    the examples.
    '''
    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    def daysBetweenDates_fails(self, date1: str, date2: str) -> int:
        def isLeapYear(year:int) -> bool:
            if year % 4 != 0:
                return False
            if year % 100 == 0:
                return year % 400 == 0
            return True
        def dateConvert(date:str) -> tuple[int]:
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[8:10])
            return (year, month, day)
        date1 = dateConvert(date1)
        date2 = dateConvert(date2)
        # answer = 365 + isLeapYear(date1[0])
        # for m in range(1, date1[1]):
        #     answer -= self.months[m]
        # answer -= date1[2]
        answer = self.months[date1[1]]
        for y in range(date1[0]+1,date2[0]):
            answer += 365 + isLeapYear(y)
        for m in range(1, date2[1]):
            answer += self.months[m]
        answer += date2[2]
        return answer

    # brute force from zero date
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        def isLeapYear(year:int) -> bool:
                    if year % 4 != 0:
                        return False
                    if year % 100 == 0:
                        return year % 400 == 0
                    return True
        def sinceStart(year:int,month:int,day:int) -> int:
            answer = 0
            for y in range(1971,year):
                answer += 365 + isLeapYear(y)
            for m in range(1,month):
                answer += months[m] + (m==2 and isLeapYear(year))
            return answer + day
        end = sinceStart(int(date2[:4]),int(date2[5:7]),int(date2[8:10]))
        start = sinceStart(int(date1[:4]),int(date1[5:7]),int(date1[8:10]))
        return max(end,start) - min(end,start)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "2019-06-29"
        j = "2019-06-30"
        o = 1
        self.assertEqual(s.daysBetweenDates(i,j), o)

    def test_two(self):
        s = Solution()
        i = "2020-01-15"
        j = "2019-12-31"
        o = 15
        self.assertEqual(s.daysBetweenDates(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)