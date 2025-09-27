# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional


class Solution:
    '''
    In a string s of lowercase letters, these letters form consecutive groups of
    the same character.

    A group is identified by an interval [start, end], where start and end
    denote the start and end indices (inclusive) of the group.

    A group is considered large if it has 3 or more characters.

    Return the intervals of every large group sorted in increasing order by
    start index.
    '''
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        answer = []
        s += "."
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if i - start - 1 >= 2:
                    answer.append([start,i-1])
                start = i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abbxxxxzzy"
        o = [[3,6]]
        self.assertEqual(s.largeGroupPositions(i), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        o = []
        self.assertEqual(s.largeGroupPositions(i), o)

    def test_three(self):
        s = Solution()
        i = "abcdddeeeeaabbbcd"
        o = [[3,5],[6,9],[12,14]]
        self.assertEqual(s.largeGroupPositions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)