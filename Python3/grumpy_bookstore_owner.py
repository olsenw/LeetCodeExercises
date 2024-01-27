# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a bookstore owner that has a store open for n minutes. Every
    minute, some number of customers enter the store. Given an integer array
    customers of length n where customers[i] is the number of the customer that
    enters the store at the start of the ith minute and all those customers
    leave after the end of that minute.

    On some minutes, the bookstore owner is grumpy. Given a binary array grumpy
    where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute,
    and is 0 otherwise.

    when the bookstore owner is grumpy, the customers of that minute are not
    satisfied, otherwise, they are satisfied.

    The bookstore owner knows a secret technique to keep themselves not grumpy
    for minutes consecutive minutes, but can only use it once.

    Return the maximum number of customers that can be satisfied throughout the
    day.
    '''
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        answer = sum(customers[:minutes]) + sum(i if not j else 0 for i,j in zip(customers[minutes:], grumpy[minutes:]))
        curr = answer
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes]:
                curr -= customers[i - minutes]
            if grumpy[i]:
                curr += customers[i]
            answer = max(answer, curr)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,1,2,1,1,7,5]
        j = [0,1,0,1,0,1,0,1]
        k = 3
        o = 16
        self.assertEqual(s.maxSatisfied(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = [0]
        k = 1
        o = 1
        self.assertEqual(s.maxSatisfied(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [5,8]
        j = [0,1]
        k = 1
        o = 13
        self.assertEqual(s.maxSatisfied(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)