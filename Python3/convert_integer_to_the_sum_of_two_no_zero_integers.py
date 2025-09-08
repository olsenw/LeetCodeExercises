# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    No-Zero integers are positive integers that do not contain any 0's in its
    decimal representation.

    Given an integer n, return a list of two integers [a,b] where:
    * a and b are No-Zero integers
    * a + b = n

    The test cases are generated so that there is at least one valid solution.
    If there are many valid solutions, return any of them.
    '''
    # catches a bunch of edges cases incorrectly
    def getNoZeroIntegers_fails(self, n: int) -> List[int]:
        n = [int(c) for c in str(n)]
        a = []
        b = []
        carry = False
        for i in reversed(n):
            if carry:
                carry = False
                i -= 1
            if i <= 1:
                carry = True
                i += 10
            if i >= 10:
                a.append(9)
                b.append(i - 9)
            else:
                a.append(i-1)
                b.append(1)
        if carry:
            a.pop()
            b.pop()
        a = int(''.join(str(i) for i in a[::-1]))
        b = int(''.join(str(i) for i in b[::-1]))
        return [a,b]

    # based on hints (which say brute force)
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def valid(n:int)->bool:
            return not ('0' in str(n))
        a = 1
        b = n - 1
        while a <= b:
            if a + b == n and valid(a) and valid(b):
                return [b,a]
            a += 1
            b -= 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = [1,1]
        self.assertEqual(s.getNoZeroIntegers(i), o)

    def test_two(self):
        s = Solution()
        i = 11
        o = [9,2]
        self.assertEqual(s.getNoZeroIntegers(i), o)

    def test_three(self):
        s = Solution()
        i = 101
        o = [89,12]
        self.assertEqual(s.getNoZeroIntegers(i), o)

    def test_four(self):
        s = Solution()
        i = 19
        o = [18,1]
        self.assertEqual(s.getNoZeroIntegers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)