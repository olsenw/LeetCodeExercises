# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array bloomDay, an integer m and an integer k.

    The goal is to make m bouquets. To make a bouquet k adjacent flowers from
    the garden.

    The garden consists of n flowers, the ith flower will bloom in the
    bloomDay[i] and then can be used in exactly one bouquet.

    Return the minimum number of days needed to wait to be able to make m
    bouquets from the garden. If it is impossible to make m bouquets return -1.
    '''
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bloom(day):
            answer = 0
            c = 0
            for bloom in bloomDay:
                if bloom > day:
                    c = 0
                else:
                    c += 1
                if c == k:
                    answer += 1
                    c = 0
            return answer >= m
        i,j = 1, max(bloomDay)
        while i < j:
            mid = i + (j - i) // 2
            if bloom(mid):
                j = mid
            else:
                i = mid + 1
        return i if bloom(i) else -1

class UnitTesting(unittest.TestCase):
    # def test_one(self):
    #     s = Solution()
    #     i = [1,10,3,10,2]
    #     j = 3
    #     k = 1
    #     o = 3
    #     self.assertEqual(s.minDays(i,j,k), o)

    # def test_two(self):
    #     s = Solution()
    #     i = [1,10,3,10,2]
    #     j = 3
    #     k = 2
    #     o = -1
    #     self.assertEqual(s.minDays(i,j,k), o)

    # def test_three(self):
    #     s = Solution()
    #     i = [7,7,7,7,12,7,7]
    #     j = 2
    #     k = 3
    #     o = 12
    #     self.assertEqual(s.minDays(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [100,100]
        j = 1
        k = 1
        o = 100
        self.assertEqual(s.minDays(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)