# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed circular string array words and a string target. A
    circular array means that the array's end connects to the array's beginning.

    Starting from startIndex, move to either the next word or the previous word
    with 1 step at a time.

    Return the shortest distance needed to reach the string target. If the
    string target does not exist in words, return -1.
    '''
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        a,b = n,n
        if words[startIndex] == target:
            return 0
        a,b = 1,1
        i = startIndex + 1
        if i == n:
            i = 0
        while i != startIndex:
            if words[i] == target:
                break
            a += 1
            i += 1
            if i == n:
                i = 0
        if a == n:
            return -1
        i = startIndex - 1
        if i == -1:
            i = n - 1
        while i != startIndex:
            if words[i] == target:
                break
            b += 1
            i -= 1
            if i == -1:
                i = n - 1
        return min(a,b) # if a != n else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["hello","i","am","leetcode","hello"]
        j = "hello"
        k = 1
        o = 1
        self.assertEqual(s.closetTarget(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","leetcode"]
        j = "leetcode"
        k = 0
        o = 1
        self.assertEqual(s.closetTarget(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = ["i","eat","leetcode"]
        j = "ate"
        k = 0
        o = -1
        self.assertEqual(s.closetTarget(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = ["hqrdflmsiv","bphfkwxwux","jwhovjrktk","masvwbrofg","bpngempqkt","bphfkwxwux","bpngempqkt","wvpoegifyu","bpngempqkt","wrgdcgwvrx"]
        j = "bpngempqkt"
        k = 1
        o = 3
        self.assertEqual(s.closetTarget(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)