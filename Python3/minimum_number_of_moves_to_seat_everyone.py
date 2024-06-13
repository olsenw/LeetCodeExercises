# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n seats and n students in a room. Given an array seats of length
    n, where seats[i] is the position of the ith seat. Also given is the array
    students of length n, where students[i] is the position of the jth student.

    The following move may be performed any number of times.
    * Increase or decrease the position of the ith student by 1 (ie moving the
      ith student from position x to x + 1 or x - 1).

    Return the minimum number of moves required to move each student to a seat
    such that no two students are in the same seat.

    Note that there may be multiple seats or students in the same position at
    the beginning.
    '''
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(i-j) for i,j in zip(seats, students))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,5]
        j = [2,7,4]
        o = 4
        self.assertEqual(s.minMovesToSeat(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,1,5,9]
        j = [1,3,2,6]
        o = 7
        self.assertEqual(s.minMovesToSeat(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,2,6,6]
        j = [1,3,2,6]
        o = 4
        self.assertEqual(s.minMovesToSeat(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)