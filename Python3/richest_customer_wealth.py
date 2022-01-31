# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n integer grid accounts where accounts[i][j] is the 
    amount of money the ith customer has in the jth bank. Return the 
    wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their
    bank accounts. The richest customer is the customer that has the
    maximum wealth.
    '''
    # O(m n) time
    # O(m) space (creates a list of customer wealth)
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts)

    # O(m n) time
    # O(1) space
    def maximumWealth_alt(self, accounts: List[List[int]]) -> int:
        s = 0
        m = 0
        for a in accounts:
            s = sum(a)
            if s > m:
                m = s
        return m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[3,2,1]]
        o = 6
        self.assertEqual(s.maximumWealth(i), o)
        self.assertEqual(s.maximumWealth_alt(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,5],[7,3],[3,5]]
        o = 10
        self.assertEqual(s.maximumWealth(i), o)
        self.assertEqual(s.maximumWealth_alt(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)