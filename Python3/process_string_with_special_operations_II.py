# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters and the special
    characters: *, #, and %.

    Also given an integer k.

    Build a new string result by processing s according to the following rules
    from left to right:
    * If the letter is a lowercase English letter append it to result.
    * A '*' removes the last character from result, if it exists.
    * A '#' duplicates the current result and appends it to itself.
    * A '%' reverses the current result.

    Return the kth character of the final string result. If k is out of bounds
    or result, return '.'.
    '''
    # fails because memory limit exceeded
    # expanded string is very large
    def processStr_memory(self, s: str, k: int) -> str:
        answer = ""
        for c in s:
            if c == '*':
                answer = answer[:-1]
            elif c == '#':
                answer += answer
            elif c == '%':
                answer = answer[::-1]
            else:
                answer += c
        if len(answer) <= k:
            return '.'
        return answer[k]

    # based on editorial
    # https://leetcode.com/problems/process-string-with-special-operations-ii/editorial/?envType=daily-question&envId=2026-06-17
    def processStr(self, s: str, k: int) -> str:
        # find length of the completed string
        length = 0
        for c in s:
            if c == '*':
                length = max(0, length-1)
            elif c == '#':
                length *= 2
            elif c == '%':
                pass
            else:
                length += 1
        # check if k is out of bounds
        if k + 1 > length:
            return "."
        # reverse string to undo operations
        for c in s[::-1]:
            # undo character removal
            if c == '*':
                length += 1
            # undo doubling of string
            elif c == '#':
                # check if k in the 2nd half of string
                if k + 1 > (length + 1) // 2:
                    k -= length // 2
                # undo doubling
                length = (length + 1) // 2
            # mirror where in string k is pointing
            elif c == '%':
                k = length - k - 1
            # remove letter
            else:
                # if this matches return letter
                if k + 1 == length:
                    return c
                length -= 1
        # default case
        return "."

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a#b%*"
        j = 1
        o = "a"
        self.assertEqual(s.processStr(i,j), o)

    def test_two(self):
        s = Solution()
        i = "cd%#*#"
        j = 3
        o = "d"
        self.assertEqual(s.processStr(i,j), o)

    def test_three(self):
        s = Solution()
        i = "z*#"
        j = 0
        o = "."
        self.assertEqual(s.processStr(i,j), o)

    def test_four(self):
        s = Solution()
        i = '%edx#n#lkc####uom##qg#%#b#ek%##%%ocr#m%#fv%i%%#n#u%%#n#q%v#rwvd##t###%#%%%o*##r#gr*gz#dm%ez'
        j = 0
        o = "."
        self.assertEqual(s.processStr(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)