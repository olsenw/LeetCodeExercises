# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, find the first non-repeating character in it and
    return its index. If it does not exist, return -1.
    '''
    def firstUniqChar_passes(self, s: str) -> int:
        d = {a:[0,-1] for a in "abcdefghijklmnopqrstuvwxyz"}
        for a,b in enumerate(s):
            d[b][0] += 1
            d[b][1] = a
        a = 10**6 + 1
        for k in d:
            if d[k][0] == 1:
                a = min(a,d[k][1])
        if a == 10**6 + 1:
            return -1
        return a

    def firstUniqChar(self, s: str) -> int:
        seen = set()
        index = dict()
        for a,b in enumerate(s):
            if b in seen:
                continue
            elif b in index:
                del index[b]
                seen.add(b)
            else:
                index[b] = a
        if not index:
            return -1
        return list(index.values())[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leetcode"
        o = 0
        self.assertEqual(s.firstUniqChar(i), o)

    def test_two(self):
        s = Solution()
        i = "loveleetcode"
        o = 2
        self.assertEqual(s.firstUniqChar(i), o)

    def test_three(self):
        s = Solution()
        i = "aabb"
        o = -1
        self.assertEqual(s.firstUniqChar(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)