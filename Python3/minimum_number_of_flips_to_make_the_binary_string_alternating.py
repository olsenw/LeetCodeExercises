# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s. It is possible to perform two types of operations
    on the string in any sequence:
    * Type-1: Remove the character at the start of the string s and append it to
      the end of the string.
    * Type-2: Pick any character in s and flip its value, ie if its value is '0'
      it becomes '1' and vice-versa.
    
    Return the minimum number of type-2 operations needed to make s alternating.

    The string is called alternating if no two adjacent characters are equal.
    '''
    # brute force O(n^2)
    def minFlips_brute(self, s: str) -> int:
        n = len(s)
        answer = n
        s = s + s
        for i in range(n):
            last = s[i]
            a = 0
            for j in range(i+1,i+n):
                if s[j] == last:
                    a += 1
                    last = '1' if s[j] == '0' else '0'
                else:
                    last = s[j]
            answer = min(answer, a)
        return answer

    def minFlips_fails(self, s: str) -> int:
        n = len(s)
        s = s + s
        evenCharacter = s[0]
        oddCharacter = '1' if evenCharacter == '0' else '0'
        evenCount = 0
        oddCount = 0
        for i in range(n):
            if i % 2 == 0 and s[i] == oddCharacter:
                oddCount += 1
            if i % 2 == 1 and s[i] == evenCharacter:
                evenCount += 1
        answer = evenCount + oddCount
        for i in range(n, len(s)):
            if i-n % 2 == 0 and s[i-n] == oddCharacter:
                oddCount -= 1
            if i-n % 2 == 1 and s[i-n] == evenCharacter:
                evenCharacter += 1
            evenCount,oddCount = oddCount,evenCount
            evenCharacter,oddCharacter = oddCharacter,evenCharacter
            if i % 2 == 0 and s[i] == oddCharacter:
                oddCount += 1
            if i % 2 == 1 and s[i] == evenCharacter:
                evenCount += 1
            answer = min(answer, evenCount + oddCount)
        return answer

    # based on comment by himanshumahtolia1 in LeetCode editorial
    # https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/editorial/?envType=daily-question&envId=2026-03-07
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        # best pattern starting with zero
        alternatingZero = "".join("1" if i % 2 == 1 else "0" for i in range(2*n))
        # best pattern starting with one
        alternatingOne = "".join("0" if i % 2 == 1 else "1" for i in range(2*n))
        # minimum number of flips
        answer = 2 * n
        # how off t is from alternatingZero/One
        diffZero = 0
        diffOne = 0
        # left side of sliding window
        left = 0
        for right in range(2 * n):
            # add right most character in sliding window
            diffZero += t[right] != alternatingZero[right]
            diffOne += t[right] != alternatingOne[right]
            # if window wider than n, remove leftmost character
            if right - left + 1 > n:
                diffZero -= t[left] != alternatingZero[left]
                diffOne -= t[left] != alternatingOne[left]
                left += 1
            # if window is size n update answer
            if right - left + 1 == n:
                answer = min(answer, diffZero, diffOne)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "111000"
        o = 2
        self.assertEqual(s.minFlips(i), o)

    def test_two(self):
        s = Solution()
        i = "010"
        o = 0
        self.assertEqual(s.minFlips(i), o)

    def test_three(self):
        s = Solution()
        i = "1110"
        o = 1
        self.assertEqual(s.minFlips(i), o)

    def test_four(self):
        s = Solution()
        i = "111000111"
        o = 3
        self.assertEqual(s.minFlips(i), o)

    def test_five(self):
        s = Solution()
        i = "1010011010"
        o = 2
        self.assertEqual(s.minFlips(i), o)

    def test_six(self):
        s = Solution()
        i = "01001001101"
        #   "01001101010"
        #       ^^
        o = 2
        self.assertEqual(s.minFlips(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)