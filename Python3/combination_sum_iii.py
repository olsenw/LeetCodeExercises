# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Find all valid combinations of k numbers that sum up to n such that
    the following conditions are true
    * Only numbers 1 through 9 are used.
    * Each number is used at most once.

    Return a list of all possible valid combinations. The list must not
    contain the same combinations twice, and the combinations may be
    returned in any order.
    '''
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        a = []
        def choice(r,t,c,o):
            if r == 0:
                if t == 0:
                    a.append(list(c))
                return
            for i, j in enumerate(o):
                if j > t:
                    return
                c.append(j)
                choice(r - 1, t - j, c, o[i + 1:])
                c.pop()
            pass
        choice(k,n,[],[1,2,3,4,5,6,7,8,9])
        return a

    def combinationSum3_alt(self, k: int, n: int) -> List[List[int]]:
        a = []
        def choice(r,t,c,o):
            if r == 1:
                if t in o:
                    a.append(c + [t])
                return
            for i, j in enumerate(o):
                if j > t:
                    return
                c.append(j)
                choice(r - 1, t - j, c, o[i + 1:])
                c.pop()
            pass
        choice(k,n,[],[1,2,3,4,5,6,7,8,9])
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 7
        o = [[1,2,4]]
        self.assertEqual(s.combinationSum3(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 9
        o = [[1,2,6],[1,3,5],[2,3,4]]
        self.assertEqual(s.combinationSum3(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = 1
        o = []
        self.assertEqual(s.combinationSum3(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)