# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A string s is called happy if it satisfies the following conditions:
    * s only contains the letters 'a', 'b', and 'c'.
    * s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    * s contains at most a occurrences of the letter 'a'.
    * s contains at most b occurrences of the letter 'b'.
    * s contains at most c occurrences of the letter 'c'.

    Given three integers a, b, c, return the longest possible happy string. If
    there are multiple longest happy strings, return any of them. If there is no
    such string, return the empty string "".

    A substring is a contiguous sequence of characters within a string.
    '''
    def longestDiverseString_fails(self, a: int, b: int, c: int) -> str:
        answer = ""
        h = []
        if a:
            heapq.heappush(h, [-a,'a'])
        if b:
            heapq.heappush(h, [-b,'b'])
        if c:
            heapq.heappush(h, [-c,'c'])
        a,b = 0,'d'
        while h:
            x,y = heapq.heappop(h)
            answer += y * -max(x, -2)
            x -= max(x,-2)
            if a:
                heapq.heappush(h, [a, b])
            a,b = x,y
        return answer

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        answer = ""
        h = []
        if a:
            heapq.heappush(h, [-a,'a'])
        if b:
            heapq.heappush(h, [-b,'b'])
        if c:
            heapq.heappush(h, [-c,'c'])
        while h:
            x,y = heapq.heappop(h)
            if answer[-2:] == y*2:
                if h:
                    a,b = heapq.heappop(h)
                    answer += b
                    if a+1 != 0:
                        heapq.heappush(h, [a+1,b])
                else:
                    break
            else:
                x += 1
                answer += y
            if x != 0:
                heapq.heappush(h, [x,y])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1,1,7
        o = "ccaccbcc"
        self.assertEqual(s.longestDiverseString(*i), o)

    def test_two(self):
        s = Solution()
        i = 7, 1, 0
        o = "aabaa"
        self.assertEqual(s.longestDiverseString(*i), o)

    def test_three(self):
        s = Solution()
        i = 7, 7, 14
        o = "ccaccbccaccbcabcabcabcabcabc"
        self.assertEqual(s.longestDiverseString(*i), o)

    def test_four(self):
        s = Solution()
        i = 0, 8, 11
        o = "ccbccbcbcbcbcbcbcbc"
        self.assertEqual(s.longestDiverseString(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)