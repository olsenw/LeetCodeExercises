# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers num1 and num2.

    In one operation, it is possible to choose an integer i in the range [0, 60]
    and subtract 2^i + num2 from num1.

    return the integer denoting the minimum number of operations needed to make
    num1 equal to 0.

    If it is impossible to make num1 equal to 0, return -1.
    '''
    # brute force trying options
    def makeTheIntegerZero_brute(self, num1: int, num2: int) -> int:
        # options = [(2**i) + num2 for i in range(60)]
        options = [(2**i) + num2 for i in range(60) if -num1 <= (2**i) + num2 <= num1]
        values = {0}
        # hint maximum number of operations is 60
        for answer in range(60):
            update = set()
            for v in values:
                for o in options:
                    if -num1 <= v + o <= num1:
                        update.add(v + o)
            if num1 in update:
                return answer + 1
            values = update
        return -1

    # based on Leetcode solution
    # https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/editorial/?envType=daily-question&envId=2025-09-05
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # number of operations being performed
        k = 1
        while True:
            # simulate the k subtractions of num2 from num1
            x = num1 - num2 * k
            # test if x can be expressed by k powers of 2
            if x < k:
                # impossible to achieve because 2^0 * k is k
                return -1
            if k >= x.bit_count():
                # able to remove every set bit from x
                return k
            k += 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = -2
        o = 3
        self.assertEqual(s.makeTheIntegerZero(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 7
        o = -1
        self.assertEqual(s.makeTheIntegerZero(i,j), o)

    def test_three(self):
        s = Solution()
        i = 100
        j = -1000
        o = 4
        self.assertEqual(s.makeTheIntegerZero(i,j), o)

    def test_three(self):
        s = Solution()
        i = 999999999
        j = -9999
        o = 18
        self.assertEqual(s.makeTheIntegerZero(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)