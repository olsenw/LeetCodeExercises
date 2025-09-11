# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A permutation perm of n + 1 integers of all the integers in the range [0, n]
    can be represented as a string s of length n where:
    * s[i] = 'I' if perm[i] < perm[i+1], and
    * s[i] = 'D' if perm[i] > perm[i+1].

    Given a string s, reconstruct the permutation perm and return it. If there
    are multiple valid permutations perm, return any of them.
    '''
    def diStringMatch(self, s: str) -> List[int]:
        answer = []
        i,j = 0,len(s)
        for k in s:
            if k == 'I':
                answer.append(i)
                i += 1
            else:
                answer.append(j)
                j -= 1
        answer.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "IDID"
        o = [0,4,1,3,2]
        self.assertEqual(s.diStringMatch(i), o)

    def test_two(self):
        s = Solution()
        i = "III"
        o = [0,1,2,3]
        self.assertEqual(s.diStringMatch(i), o)

    def test_three(self):
        s = Solution()
        i = "DDI"
        o = [3,2,0,1]
        self.assertEqual(s.diStringMatch(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)