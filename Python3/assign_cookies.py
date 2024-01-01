# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Assume that an awesome parent wants to give their children some cookies.
    But, each child should only get one cookie.

    Each child i has a greed factor g[i], which is the minimum size of a cookie
    that the child will be content with; and each cookie j has a size s[j]. If
    s[j] >= g[i], the child will be content with the assignment.

    Maximize the number of content children and output the maximum number.
    '''
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m,n = len(g), len(s)
        g.sort()
        s.sort()
        answer = 0
        i,j = 0,0
        while i < m and j < n:
            if s[j] >= g[i]:
                i += 1
                answer += 1
            j += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = [1,1]
        o = 1
        self.assertEqual(s.findContentChildren(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = [1,2,3]
        o = 2
        self.assertEqual(s.findContentChildren(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)