# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s of lowercase English letters and a 2D integer array shifts
    where shifts[i] = [starti, endi, directioni]. For every i, shift the
    characters in s from the index starti to the index endi (inclusive) forward
    if directioni = 1, or shift all the characters backward if directioni = 0.

    Shifting a character forward means replacing it with the next letter in the
    alphabet (wrapping around so that 'z' becomes 'a'). Similaryl, shifting a
    character backward means replacing it with the previous letter in the
    alphabet (wrapping around so that 'a' becomes 'z').

    Return the final string after all such shifts to s are applied
    '''
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifts.sort()
        j = 0
        heap = []
        edit = 0
        answer = ""
        for i in range(len(s)):
            while j < len(shifts) and i == shifts[j][0]:
                edit += 1 if shifts[j][2] == 1 else -1
                heapq.heappush(heap, shifts[j][1:])
                j += 1
            answer += chr(((ord(s[i]) - 97 + edit) % 26) + 97)
            while heap and i == heap[0][0]:
                edit += 1 if heapq.heappop(heap)[1] == 0 else -1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        j = [[0,1,0],[1,2,1],[0,2,1]]
        o = "ace"
        self.assertEqual(s.shiftingLetters(i,j), o)

    def test_two(self):
        s = Solution()
        i = "dztz"
        j = [[0,0,0],[1,1,1]]
        o = "catz"
        self.assertEqual(s.shiftingLetters(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)