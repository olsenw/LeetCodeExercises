# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string n representing an integer, return the closest integer (not
    including itself), which is a palindrome. If there is a tie, return the
    smaller one.

    The closest is defined as the absolute difference minimized between two
    integers.
    '''
    # brute force
    def nearestPalindromic_tle(self, n: str) -> str:
        def isPalindrome(s:int) -> bool:
            s = str(s)
            return s == s[::-1]
        x = int(n) - 1
        while not isPalindrome(x):
            x -= 1
        y = int(n)
        for i in range(1,y-x):
            if isPalindrome(y + i):
                return str(y + i)
        return str(x)

    # based on Leetcode solution
    # https://leetcode.com/problems/find-the-closest-palindrome/editorial/?envType=daily-question&envId=2024-08-24
    def nearestPalindromic(self, n: str) -> str:
        def helper(mirror:int, even:bool) -> int:
            answer = mirror
            if not even:
                mirror //= 10
            while mirror > 0:
                answer = answer * 10 + mirror % 10
                mirror //= 10
            return answer
        # locate the midpoint
        i = len(n) // 2 - 1 if len(n) % 2 == 0 else len(n) // 2
        # get the first half of n
        f = int(n[:i+1])
        candidates = [
            # flip the first half to form palindrome
            helper(f, len(n) % 2 == 0),
            # check if incrementing middle bit results in palindrome
            helper(f + 1, len(n) % 2 == 0),
            # check if decrementing middle bit results in palindrome
            helper(f - 1, len(n) % 2 == 0),
            # check if 99..99 is closest
            10**(len(n) - 1) - 1,
            # check if 100..001 is closest
            10**len(n) + 1
        ]
        n = int(n)
        best = float('inf')
        answer = 0
        for c in candidates:
            if c == n:
                continue
            if abs(c - n) < best:
                best = abs(c - n)
                answer = c
            elif abs(c - n) == best:
                answer = min(answer, c)
        return str(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "123"
        o = "121"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_two(self):
        s = Solution()
        i = "1"
        o = "0"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_three(self):
        s = Solution()
        i = "12932"
        o = "12921"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_four(self):
        s = Solution()
        i = "99800"
        o = "99799"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_five(self):
        s = Solution()
        i = "12120"
        o = "12121"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_six(self):
        s = Solution()
        i = "1234"
        o = "1221"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_seven(self):
        s = Solution()
        i = "999"
        o = "1001"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_eight(self):
        s = Solution()
        i = "1000"
        o = "999"
        self.assertEqual(s.nearestPalindromic(i), o)

    def test_nine(self):
        s = Solution()
        i = "807045053224792883"
        o = "807045053350540708"
        self.assertEqual(s.nearestPalindromic(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)