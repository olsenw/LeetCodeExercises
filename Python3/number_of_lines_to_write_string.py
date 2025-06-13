# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s of lowercase English letters and an array widths denoting
    how many pixels wide each lowercase English letter is. Specifically,
    widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

    Write string s across several lines, where each line is no longer than 100
    pixels. Starting at the beginning of s, write as many letters on the first
    line such that the total width does not exceed 100 pixels. Then continue
    writing as many letters as possible on the second line. Continue this
    process until all characters of s have been written.

    Return an array result of length 2 where:
    * result[0] is the total number of lines.
    * result[1] is the width of the last line in pixels.
    '''
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lineWidth = 100
        lines = 1
        characters = lineWidth
        for c in s:
            c = widths[ord(c) - 97]
            if characters < c:
                characters = lineWidth
                lines += 1
            characters -= c
        return [lines, lineWidth - characters]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        j = "bbbcccdddaaa"
        o = [2,4]
        self.assertEqual(s.numberOfLines(i,j), o)

    def test_two(self):
        s = Solution()
        i = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        j = "abcdefghijklmnopqrstuvwxyz"
        o = [3,60]
        self.assertEqual(s.numberOfLines(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)