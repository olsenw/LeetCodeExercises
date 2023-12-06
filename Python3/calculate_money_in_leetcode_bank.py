# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Hercy wants to save money for his first car. He puts money in the Leetcode
    bank every day.

    He starts by putting in $1 on Monday, the first day. Every day from Tuesday
    to Sunday, he will put in $1 more than the day before. On every subsequent
    Monday, he will put in $1 more than the previous Monday.

    Given n, return the total amount of money he will have in the Leetcode bank
    at the end of the nth day.
    '''
    def totalMoney_works(self, n: int) -> int:
        answer = 0
        c = 0
        for i in range(n):
            a = i % 7
            if a == 0:
                c += 1
            answer += c + a
        return answer

    # math solution 
    # based on LeetCode Editorial
    # https://leetcode.com/problems/calculate-money-in-leetcode-bank/editorial/?envType=daily-question&envId=2023-12-06
    def totalMoney(self, n: int) -> int:
        k = n // 7
        f = 28
        l = 28 + (k - 1) * 7
        s = k * (f + l) // 2
        m = 1 + k
        w = 0
        for d in range(n % 7):
            w += m + d
        return s + w

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = 10
        self.assertEqual(s.totalMoney(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 37
        self.assertEqual(s.totalMoney(i), o)

    def test_three(self):
        s = Solution()
        i = 20
        o = 96
        self.assertEqual(s.totalMoney(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)