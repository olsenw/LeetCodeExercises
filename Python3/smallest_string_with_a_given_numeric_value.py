# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The numeric value of a lowercase character is defined as its
    position (1-indexed) in the alphabet, so the numeric value of a is
    1, the numeric value of b is 2, the numeric value of c is 3, and so
    on.

    The numeric value of a string consisting of lowercase character is
    defined as the sum of its characters' numeric values.

    Given two integers n and k. Return the lexicographically smallest
    string with length equal to n and numeric value equal to k.

    Note that a string x is lexicographically smaller than string y if x
    comes before y in dictionary order, that is, either x is a prefix of
    y, or x[i] < y[i] for some index i.
    '''
    def getSmallestString(self, n: int, k: int) -> str:
        z = k // 26
        k -= z * 26
        n -= z
        s = 'z' * z
        while n > k:
            s = s[1:]
            k += 26
            n += 1
        if n == k:
            return 'a' * k + s
        else:
            a = n - 1
            m = k - a
            return 'a' * a + chr(m + 96) + s

    # logic error
    def getSmallestString_fails_wrong(self, n: int, k: int) -> str:
        s = ''
        # go through most expensive letters first
        for i in range(26,0,-1):
            # haw many go in
            num = k // i
            k -= num * i
            n -= num
            # update string
            s = chr(i + 96) * num + s
            # need more points refund last letter
            if n > k:
                s = s[1:]
                k += i
                n += 1
            # have enough 'a' to fill
            elif n == k:
                return 'a' * n + s

    # time limit exceeded 69/93 cases
    def getSmallestString_fails(self, n: int, k: int) -> str:
        s = ''
        k -= n
        for _ in range(n):
            k += 1
            # character replacing 'a'
            c = min(26, k)
            k -= c
            s = chr(c + 96) + s
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 27
        o = "aay"
        self.assertEqual(s.getSmallestString(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 73
        o = "aaszz"
        self.assertEqual(s.getSmallestString(i,j), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = 25
        o = "y"
        self.assertEqual(s.getSmallestString(i,j), o)

    def test_four(self):
        s = Solution()
        i = 4
        j = 30
        o = "aabz"
        self.assertEqual(s.getSmallestString(i,j), o)

    def test_five(self):
        s = Solution()
        i = 67
        j = 882
        o = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaapzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        self.assertEqual(s.getSmallestString(i,j), o)

    def test_six(self):
        s = Solution()
        i = 5
        j = 130
        o = "zzzzz"
        self.assertEqual(s.getSmallestString(i,j), o)

    def test_seven(self):
        s = Solution()
        i = 80
        j = 576
        o = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaavzzzzzzzzzzzzzzzzzzz"
        self.assertEqual(s.getSmallestString(i,j), o)

    def test_eight(self):
        s = Solution()
        i = 9
        j = 34
        o = "aaaaaaaaz"
        self.assertEqual(s.getSmallestString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)