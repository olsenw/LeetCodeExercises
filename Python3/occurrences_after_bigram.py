# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings first and second, consider occurrences in some text of the
    form "first second third", where second comes immediately after first, and
    third comes immediately after second.

    Return an array of all the words third for each occurrence of "first second
    third".
    '''
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        answer = []
        text = text.split()
        n = len(text)
        for i in range(2,n):
            if text[i-2] == first and text[i-1] == second:
                answer.append(text[i])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "alice is a good girl she is a good student"
        j = "a"
        k = "good"
        o = ["girl","student"]
        self.assertEqual(s.findOcurrences(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "alice is a good girl she is a good student"
        j = "a"
        k = "good"
        o = ["girl","student"]
        self.assertEqual(s.findOcurrences(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)