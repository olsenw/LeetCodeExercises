# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A string originalText is encoded using a slanted transposition cipher to a
    string encodedText with the help of a matrix having a fixed number of rows
    rows.

    originalText is placed first in a top-left to bottom-right manner.
    (Picture online)

    The blue cells are filled first, followed by the red cells, then the yellow
    cells, and so on, until the end of originalText. The arrow indicates the
    order in which the cells are filled. All empty cells are filled with ' '.
    The number of columns is chosen such that the rightmost column will not be
    empty after filling in originalText.

    encodedText is then formed by appending all characters of the matrix in a
    row-wise fashion.
    (Picture online)

    The characters in the blue cells are appended first to encodedText, then the
    red cells, and so on, and finally the yellow cells. The arrow indicates the
    order in which the cells are accessed.

    Given the encoded string encodedText and number of rows, return the original
    string originalText.

    Note: originalText does not have any trailing spaces ' '. The test cases are
    generated such that there is only one possible originalText.
    '''
    def decodeCiphertext_slow(self, encodedText: str, rows: int) -> str:
        m = rows
        n = len(encodedText) // m
        encoded = [[' '] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                encoded[i][j] = encodedText[(i*n) + j]
        answer = ""
        for j in range(n):
            # if i + j >= n:
            #     break
            for i in range(m):
                if i+j >= n:
                    break
                answer += encoded[i][i+j]
        return answer.rstrip()

    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        m = rows
        n = len(encodedText) // m
        answer = ""
        for j in range(n):
            for i in range(m):
                if i+j >= n:
                    break
                answer += encodedText[(i*n) + i + j]
        return answer.rstrip()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ch   ie   pr"
        j = 3
        o = "cipher"
        self.assertEqual(s.decodeCiphertext(i,j), o)

    def test_two(self):
        s = Solution()
        i = "iveo    eed   l te   olc"
        j = 4
        o = "i love leetcode"
        self.assertEqual(s.decodeCiphertext(i,j), o)

    def test_three(self):
        s = Solution()
        i = "coding"
        j = 1
        o = "coding"
        self.assertEqual(s.decodeCiphertext(i,j), o)

    def test_four(self):
        s = Solution()
        i = " b  ac"
        j = 2
        o = " abc"
        self.assertEqual(s.decodeCiphertext(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)