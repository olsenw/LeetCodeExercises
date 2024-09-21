# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    # stuck in details
    # basic idea is sound
    def shortestPalindrome_incomplete(self, s: str) -> str:
        n = len(s)
        mid = n // 2
        base = 26
        mod = 10*9 + 7
        # Precompute powers of base % mod
        power = [1] (mid + 1)
        for i in range(1, mid + 1):
            power[i] = (power[i-1] * base) % mod
        # intial hash of left side of string
        left = 0
        for i in range(mid + 1):
            left = (left * base + ord(s[i])) % mod
        # intial hash of right side of string
        right = 0
        for i in range(n-1,mid - 1,-1):
            right = (right * base + ord(s[i])) % mod
        # compare rolling hashes of decreasing size
        for i in range(mid):
            left -= power[i] * ord(s[i]) % mod
            right -= power[mid + i] * ord(s[mid + i]) % mod
            right -= power[mid + i - 1] * ord(s[mid + i - 1]) % mod
            right = right * base + ord(s[mid + i - 2]) % mod
            if left == right:
                return 
        return

    # based on leetcode rolling hash solution
    # https://leetcode.com/problems/shortest-palindrome/editorial/?envType=daily-question&envId=2024-09-20
    def shortestPalindrome(self, s: str) -> str:
        hash_base = 29
        mod_value = int(1e9 + 7)
        forward_hash = 0
        reverse_hash = 0
        power_value = 1
        palindrome_end_index = -1

        # Calculate rolling hashes and find the longest palindromic prefix
        for i, current_char in enumerate(s):
            # Update forward hash
            forward_hash = (
                forward_hash * hash_base + (ord(current_char) - ord("a") + 1)
            ) % mod_value

            # Update reverse hash
            reverse_hash = (
                reverse_hash + (ord(current_char) - ord("a") + 1) * power_value
            ) % mod_value
            power_value = (power_value * hash_base) % mod_value

            # If forward and reverse hashes match, update palindrome end index
            if forward_hash == reverse_hash:
                palindrome_end_index = i

        # Find the remaining suffix after the longest palindromic prefix
        suffix = s[palindrome_end_index + 1 :]

        # Reverse the remaining suffix
        reversed_suffix = suffix[::-1]

        # Prepend the reversed suffix to the original string and return the result
        return reversed_suffix + s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aacecaaa"
        o = "aaacecaaa"
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        o = "dcbabcd"
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)