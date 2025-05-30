# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and a character c that occurs in s, return an array of
    integers answer where answer.length == s.length and answer[i] is the
    distance from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i -j), where abs is the
    absolute value function.
    '''
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [-10**5]
        for i,j in enumerate(s):
            if j == c:
                indices.append(i)
        indices.append(10**5)
        answer = []
        index = 1
        for i in range(len(s)):
            if i > indices[index]:
                index += 1
            answer.append(min(abs(indices[index-1] - i), abs(indices[index] - i)))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "loveleetcode"
        j = "e"
        o = [3,2,1,0,1,0,0,1,2,2,1,0]
        self.assertEqual(s.shortestToChar(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aaab"
        j = "b"
        o = [3,2,1,0]
        self.assertEqual(s.shortestToChar(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)