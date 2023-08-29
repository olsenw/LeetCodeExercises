# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a customer log of a shop represented by a 0-indexed string customers
    consisting only of characters 'N' and 'Y':
    * if the ith character is 'Y', it means that customers come at the ith hour
    * whereas 'N' indicates that no customers come at the ith hour.

    If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated
    as follows:
    * For every hour when the shop is open and no customers come, the penalty
      increases by 1.
    * For every hour when the shop is closed and customers come, the penalty
      increases by 1.

    Return the earliest hour at which the shop must be closed to incur a minimum
    penalty.

    Note that if a shop closes at the jth hour, it means the shop is closed at
    the hour j.
    '''
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        y = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            y[i] = y[i+1]
            if customers[i] == 'Y':
                y[i] += 1
        answer = (0, y[0])
        m = 0
        for i in range(n):
            c = m + y[i]
            if answer[1] > c:
                answer = (i, c)
            if customers[i] == 'N':
                m += 1
        if answer[1] > m:
            answer = (n, m)
        return answer[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "YYNY"
        o = 2
        self.assertEqual(s.bestClosingTime(i), o)

    def test_two(self):
        s = Solution()
        i = "NNNNN"
        o = 0
        self.assertEqual(s.bestClosingTime(i), o)

    def test_three(self):
        s = Solution()
        i = "YYYY"
        o = 4
        self.assertEqual(s.bestClosingTime(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)