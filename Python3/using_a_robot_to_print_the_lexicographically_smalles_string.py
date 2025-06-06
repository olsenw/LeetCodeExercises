# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and a robt that currently holds an empty string t. Apply
    one of the following operations until s and t are both empty:
    * Remove the first character of a string s and give it to the robot. The
      robot will append this character to the string t.
    * Remove the last character of a string t and give it to the robot. The
      robot will write this character on paper.
    
    Return the lexicographically smallest string that can be written on the
    paper.
    '''
    # wrong see test case three
    def robotWithString_wrong(self, s: str) -> str:
        answer = ""
        # put the biggest possible character on stack
        stack = [chr(ord('z') + 1)]
        for c in s:
            pass
            while c > stack[-1]:
                answer += stack.pop()
            stack.append(c)
        while len(stack) > 1:
            answer += stack.pop()
        return answer

    # issues but closer to working idea
    def robotWithString_wrong(self, s: str) -> str:
        answer = ""
        stack = []
        c = Counter(s)
        l = min(c)
        for i in s:
            c[i] -= 1
            stack.append(i)
            while stack and stack[-1] <= l:
                answer += stack.pop()
                if c[l] == 0:
                    del c[l]
                    l = min(c)
        return answer

    def robotWithString(self, s: str) -> str:
        n = len(s)
        s += "{"
        answer = ""
        stack = []
        remain = Counter(s)
        l = min(remain)
        for i in range(n):
            pass
            stack.append(s[i])
            remain[s[i]] -= 1
            if remain[s[i]] == 0:
                del remain[s[i]]
            while stack and stack[-1] <= l:
                j = stack.pop()
                answer += j
                if j not in remain:
                    l = min(remain)
        while stack:
            answer += stack.pop()
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "zza"
        o = "azz"
        self.assertEqual(s.robotWithString(i), o)

    def test_two(self):
        s = Solution()
        i = "bac"
        o = "abc"
        self.assertEqual(s.robotWithString(i), o)

    def test_three(self):
        s = Solution()
        i = "bdda"
        o = "addb"
        self.assertEqual(s.robotWithString(i), o)

    def test_four(self):
        s = Solution()
        i = "vzhofnpo"
        o = "fnohopzv"
        self.assertEqual(s.robotWithString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)