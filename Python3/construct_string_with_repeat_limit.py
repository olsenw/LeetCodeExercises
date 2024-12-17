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
    Given a string s and an integer repeatLimit. Construct a new string
    repeatLimitedString using the characters of s such that no letter appears
    more than repeatLimit times in a row. Not all characters need to by used
    from s.

    Return the lexicographically largest repeatLimitedString possible.
    '''
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        answer = ""
        a,b = 0,0
        c = Counter(s)
        heap = [(-ord(i),j) for i,j in c.items()]
        heapq.heapify(heap)
        while heap:
            x,y = heapq.heappop(heap)
            if x == a and b == repeatLimit:
                if heap:
                    x,y = heapq.heapreplace(heap, (x,y))
                else:
                    return answer
            if x != a:
                a,b = x,0
            b += 1
            answer += chr(-x)
            if y-1 > 0:
                heapq.heappush(heap, (x,y-1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "cczazcc"
        j = 3
        o = "zzcccac"
        self.assertEqual(s.repeatLimitedString(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aababab"
        j = 2
        o = "bbabaa"
        self.assertEqual(s.repeatLimitedString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)