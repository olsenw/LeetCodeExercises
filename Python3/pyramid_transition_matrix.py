# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are blocks being stacked to form a pyramid. Each block has a color,
    which is represented by a single letter. Each row of blocks contains one
    less block than the row beneath it and is centered on top.

    To make a pyramid aesthetically pleasing, there are only specific triangular
    patterns that are allowed. A triangular pattern consists of a single block
    stacked on top of two blocks. The patterns are given as a list of
    three-letter strings allowed, where the first two characters of a pattern
    represent the left and right bottom blocks respectively, and the third
    character is the top block.

    Starting with a bottom row of blocks bottom, given as a single string, that
    must be used as the base of the pyramid.

    Given bottom and allowed, return true if it is possible to build the pyramid
    all the way to the top such that every triangular pattern in the pyramid is
    in allowed, or false otherwise.
    '''
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        patterns = defaultdict(list)
        for s in allowed:
            patterns[s[:2]].append(s[2])
        # the cache is important to save time
        @cache
        def backtrack(last:str) -> bool:
            if len(last) == 1:
                return True
            possible = [""]
            for i in range(len(last) - 1):
                p = []
                for j in patterns[last[i:i+2]]:
                    for k in possible:
                        p.append(k + j)
                possible = p
            return any(backtrack(p) for p in possible)
        return backtrack(bottom)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "BCD"
        j = ["BCC","CDE","CEA","FFF"]
        o = True
        self.assertEqual(s.pyramidTransition(i,j), o)

    def test_two(self):
        s = Solution()
        i = "AAAA"
        j = ["AAB","AAC","BCD","BBE","DEF"]
        o = False
        self.assertEqual(s.pyramidTransition(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)