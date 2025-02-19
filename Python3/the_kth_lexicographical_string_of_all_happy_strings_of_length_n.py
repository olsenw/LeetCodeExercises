# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A happy string is a string that:
    * consists only of letters of the set ['a', 'b', 'c'].
    * s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
      1-indexed).
    
    Given two integers n and k, consider a list of all happy strings of length n
    sorted in lexicographical order.

    Return the kth string of this list or return an empty string if there are
    less than k happy strings of length n.
    '''
    def getHappyString(self, n: int, k: int) -> str:
        answer = []
        def backtrack(track):
            if track == k:
                return track
            if len(answer) == n:
                return track + 1
            for c in "abc":
                if len(answer) > 0 and answer[-1] == c:
                    continue
                answer.append(c)
                track = backtrack(track)
                if track == k:
                    return track
                answer.pop()
            return track
        backtrack(0)
        return "".join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1,3
        o = "c"
        self.assertEqual(s.getHappyString(*i), o)

    def test_two(self):
        s = Solution()
        i = 1,4
        o = ""
        self.assertEqual(s.getHappyString(*i), o)

    def test_three(self):
        s = Solution()
        i = 3,9
        o = "cab"
        self.assertEqual(s.getHappyString(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)