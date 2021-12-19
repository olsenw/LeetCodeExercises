# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string
    inside the square brackets is being repeated exactly k times. Note
    that k is guaranteed to be a positive integer.

    It is assumed that the input string is always valid. (ie not extra
    white spaces, square brackets are well formed, etc)

    It is assumed that the original data does not contain any digits and
    that digits are only for those repeat numbers k.
    '''
    def decodeString(self, s: str) -> str:
        from collections import deque
        stack = deque()
        stack.append(['1',""])
        n = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                n += s[i]
            elif s[i] == '[':
                stack.append([n,""])
                n = ""
            elif s[i] == ']':
                p = stack.pop()
                for j in range(int(p[0])):
                    stack[len(stack)-1][1] += p[1]
            else:
                stack[len(stack)-1][1] += s[i]
        # p = stack.pop()[1]
        return stack.pop()[1]

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_two(self):
        s = Solution()
        self.assertEqual(s.decodeString("3[a2[c]]"), "accaccacc")

    def test_three(self):
        s = Solution()
        self.assertEqual(s.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_four(self):
        s = Solution()
        self.assertEqual(s.decodeString("abc3[cd]xyz"), "abccdcdcdxyz")

    def test_five(self):
        s = Solution()
        self.assertEqual(s.decodeString("100[leetcode]"), "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode")

if __name__ == '__main__':
    unittest.main(verbosity=2)