# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, rearrange the characters of s so that any two adjacent
    characters are not the same.

    Return any possible rearrangement of s or return "" if not possible.
    '''
    # does not handle cases like aabcc correctly
    def reorganizeString_wrong(self, s: str) -> str:
        if len(s) == 1:
            return s
        c = Counter(s)
        c = "".join([b*a for a,b in c.most_common()])
        answer = ""
        i, j = 0, len(c)-1
        while i < j:
            if c[i] == c[j]:
                return ""
            answer += c[i] + c[j]
            i += 1
            j -= 1
        if i == j:
            if answer[-1] == c[i]:
                return ""
            answer += c[i]
        return answer

    # now im thinking with heaps
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        h = [[-b,a] for a,b in c.items()]
        heapq.heapify(h)
        answer = ""
        while len(h) > 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            answer += a[1] + b[1]
            if a[0] + 1 < 0:
                heapq.heappush(h, [a[0]+1, a[1]])
            if b[0] + 1 < 0:
                heapq.heappush(h, [b[0]+1, b[1]])
        if len(h) == 1:
            if h[0][0] != -1:
                return ""
            answer += h[0][1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aab"
        o = "aba"
        self.assertEqual(s.reorganizeString(i), o)

    def test_two(self):
        s = Solution()
        i = "aaab"
        o = ""
        self.assertEqual(s.reorganizeString(i), o)

    def test_three(self):
        s = Solution()
        i = "a"
        o = "a"
        self.assertEqual(s.reorganizeString(i), o)

    def test_four(self):
        s = Solution()
        i = "aabcc"
        o = "acabc"
        self.assertEqual(s.reorganizeString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)