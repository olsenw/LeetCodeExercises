# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s and a positive integer k.

    Return the length of the longest subsequence of s that makes up a binary
    number less than or equal to k.

    Note:
    * The subsequence can contain leading zeros.
    * The empty string is considered to be equal to 0.
    * A subsequence is a string that can be derived from another string by
      deleting some or no character without changing the order of the remaining
      characters.
    '''
    # continuous subsequence... which is not the problem
    def longestSubsequence_fails(self, s: str, k: int) -> int:
        s = s[::-1]
        answer = 0
        running = 0
        left = 0
        for right in range(len(s)):
            running <<= 1
            running += s[right] == '1'
            while running > k:
                running >>= 1
                left += 1
            answer = max(answer, right - left)
        return answer

    # hint gives away greed solution
    # slow implementation
    def longestSubsequence(self, s: str, k: int) -> int:
        answer = ""
        for c in s:
            answer += c
            while int(answer, 2) > k:
                i = answer.find('1')
                answer = answer[:i] + answer[i+1:]
            pass
        return len(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1001010"
        j = 5
        o = 5
        self.assertEqual(s.longestSubsequence(i,j), o)

    def test_two(self):
        s = Solution()
        i = "00101001"
        j = 1
        o = 6
        self.assertEqual(s.longestSubsequence(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)